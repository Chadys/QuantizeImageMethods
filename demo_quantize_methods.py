import timeit
from collections import Counter
from typing import Callable, Tuple, Optional, Union, List, Type

from PIL import Image
import cv2
import numpy as np
import scipy.cluster
from sklearn.cluster import KMeans, MeanShift, MiniBatchKMeans
import sklearn.utils

# import sklearn.metrics
from pyclustering.cluster import (
    bsas,
    mbsas,
    dbscan,
    optics,
    syncnet,
    syncsom,
    ttsas,
    xmeans,
    center_initializer,
    elbow,
    kmeans,
    kmedians,
)
from pyclustering.utils import type_metric, distance_metric

MAX_SIZE = 500


def test_pillow(
    img_input: Image.Image, method: int
) -> Tuple[Type[Image.Image], List[List[int]]]:
    img: Image.Image = img_input.copy()
    img.thumbnail((MAX_SIZE, MAX_SIZE), Image.NEAREST)

    threshold_pixel_percentage: float = 0.05
    nb_colours: int = 20
    nb_colours_under_threshold: int
    nb_pixels: int = img.width * img.height
    quantized_img: Image.Image

    while True:
        # method 0 = median cut 1 = maximum coverage 2 = fast octree
        quantized_img = img.quantize(colors=nb_colours, method=method, kmeans=0)
        nb_colours_under_threshold = 0
        colours_list: [Tuple[int, int]] = quantized_img.getcolors(nb_colours)
        for (count, pixel) in colours_list:
            if count / nb_pixels < threshold_pixel_percentage:
                nb_colours_under_threshold += 1
        if nb_colours_under_threshold == 0:
            break
        nb_colours -= -(-nb_colours_under_threshold // 2)  # ceil integer division
    palette: [int] = quantized_img.getpalette()
    colours_list: [[int]] = [palette[i : i + 3] for i in range(0, nb_colours * 3, 3)]
    return quantized_img, colours_list


def test_pillow_median_cut(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], List[List[int]]]:
    return test_pillow(img_input, 0)


def test_pillow_maximum_coverage(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], List[List[int]]]:
    return test_pillow(img_input, 1)


def test_pillow_fast_octree(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], List[List[int]]]:
    return test_pillow(img_input, 2)


def get_img_data(
    img_input: Image.Image,
    mini: bool = False,
    conversion_method: int = cv2.COLOR_RGB2BGR,
) -> Tuple[np.ndarray, int, np.ndarray]:
    img: np.ndarray = cv2.cvtColor(np.array(img_input), conversion_method)
    ratio: float = min(
        MAX_SIZE / img.shape[0], MAX_SIZE / img.shape[1]
    )  # calculate ratio
    if mini:
        ratio /= 6
    img = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)

    nb_pixels: int = img.size

    flat_img: np.ndarray = img.reshape((-1, 3))
    flat_img: np.ndarray = np.float32(flat_img)
    return img, nb_pixels, flat_img


def process_result(
    center: np.ndarray,
    label: np.ndarray,
    shape: Tuple[int, int, int],
    conversion_method: int = cv2.COLOR_BGR2RGB,
) -> Tuple[Type[Image.Image], np.ndarray]:
    center: np.ndarray = np.uint8(center)
    quantized_img: np.ndarray = center[label]
    quantized_img = quantized_img.reshape(shape)
    quantized_img = cv2.cvtColor(quantized_img, conversion_method)
    center = cv2.cvtColor(np.expand_dims(center, axis=0), conversion_method)[0]
    return Image.fromarray(quantized_img), center


def update_nb_colours(
    label: np.ndarray,
    nb_pixels: int,
    threshold_pixel_percentage: float,
    nb_colours: int,  # , flat_img: np.ndarray
) -> Tuple[int, int]:
    nb_colours_under_threshold: int = 0
    label = label.flatten()
    colour_count: Counter[int] = Counter(label)
    for (pixel, count) in colour_count.items():
        if count / nb_pixels < threshold_pixel_percentage:
            nb_colours_under_threshold += 1
    # silhouette = sklearn.metrics.silhouette_score(flat_img, label, metric='euclidean', sample_size=1000)
    # print(f'nb_colours = {nb_colours}, silhouette_score = {silhouette}')
    nb_colours -= -(-nb_colours_under_threshold // 2)  # ceil integer division
    return nb_colours, nb_colours_under_threshold


def test_opencv(
    img_input: Image.Image, method1: int, method2: int
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input, False, method1)

    threshold_pixel_percentage: float = 0.01
    nb_colours: int = 20
    nb_colours_under_threshold: int = nb_colours
    criteria: Tuple[int, int, float] = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        10,
        1.0,
    )
    center: Optional[np.ndarray] = None
    label: Optional[np.ndarray] = None

    while nb_colours_under_threshold > 0:
        ret: float
        ret, label, center = cv2.kmeans(
            flat_img, nb_colours, None, criteria, 10, cv2.KMEANS_PP_CENTERS
        )
        nb_colours, nb_colours_under_threshold = update_nb_colours(
            label, nb_pixels, threshold_pixel_percentage, nb_colours  # , flat_img
        )

    return process_result(center, label, img.shape, method2)


def test_opencv_rgb(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_opencv(img_input, cv2.COLOR_RGB2BGR, cv2.COLOR_BGR2RGB)


def test_opencv_hsv(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_opencv(img_input, cv2.COLOR_RGB2HSV, cv2.COLOR_HSV2RGB)


def test_opencv_lab(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_opencv(img_input, cv2.COLOR_RGB2Lab, cv2.COLOR_Lab2RGB)


def test_scipy(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)

    # minimum percentage of image coverage each colour needs to be, lower for more colours
    threshold_pixel_percentage: float = 0.02
    nb_colours: int = 20
    nb_colours_under_threshold: int = nb_colours
    centroids: Optional[np.ndarray] = None
    qnt: Optional[np.ndarray] = None

    while nb_colours_under_threshold > 0:
        # performing the clustering
        centroids, _ = scipy.cluster.vq.kmeans(flat_img, nb_colours)
        # quantization
        qnt, _ = scipy.cluster.vq.vq(flat_img, centroids)
        nb_colours, nb_colours_under_threshold = update_nb_colours(
            qnt, nb_pixels, threshold_pixel_percentage, nb_colours  # , flat_img
        )

    # reshaping the result of the quantization
    centers_idx: np.ndarray = np.reshape(qnt, (img.shape[0], img.shape[1]))
    return process_result(centroids, centers_idx, img.shape)


def test_scipy2(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)

    # minimum percentage of image coverage each colour needs to be, lower for more colours
    threshold_pixel_percentage: float = 0.02
    nb_colours: int = 20
    nb_colours_under_threshold: int = nb_colours
    centroids: Optional[np.ndarray] = None
    qnt: Optional[np.ndarray] = None

    flat_img_sample: np.ndarray = sklearn.utils.shuffle(flat_img, random_state=0)[:1000]

    while nb_colours_under_threshold > 0:
        # performing the clustering
        centroids, _ = scipy.cluster.vq.kmeans(flat_img_sample, nb_colours)
        # quantization
        qnt, _ = scipy.cluster.vq.vq(flat_img, centroids)
        nb_colours, nb_colours_under_threshold = update_nb_colours(
            qnt, nb_pixels, threshold_pixel_percentage, nb_colours  # , flat_img
        )

    # reshaping the result of the quantization
    centers_idx: np.ndarray = np.reshape(qnt, (img.shape[0], img.shape[1]))
    return process_result(centroids, centers_idx, img.shape)


def test_sklearn_kmeans(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)

    # minimum percentage of image coverage each colour needs to be, lower for more colours
    threshold_pixel_percentage: float = 0.02
    nb_colours: int = 20
    nb_colours_under_threshold: int = nb_colours
    center: Optional[np.ndarray] = None
    label: Optional[np.ndarray] = None

    while nb_colours_under_threshold > 0:
        kmeans_instance: KMeans = KMeans(n_clusters=nb_colours, random_state=0).fit(
            flat_img
        )
        label = kmeans_instance.labels_
        center = kmeans_instance.cluster_centers_
        nb_colours, nb_colours_under_threshold = update_nb_colours(
            label, nb_pixels, threshold_pixel_percentage, nb_colours  # , flat_img
        )

    return process_result(center, label, img.shape)


def test_sklearn_iter(
    img_input: Image.Image, constructor: Callable
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)

    # minimum percentage of image coverage each colour needs to be, lower for more colours
    threshold_pixel_percentage: float = 0.02
    nb_colours: int = 20
    nb_colours_under_threshold: int = nb_colours
    center: Optional[np.ndarray] = None
    label: Optional[np.ndarray] = None

    flat_img_sample: np.ndarray = sklearn.utils.shuffle(flat_img, random_state=0)[:1000]

    while nb_colours_under_threshold > 0:
        kmeans_instance: Union[KMeans, MiniBatchKMeans] = constructor(
            n_clusters=nb_colours, random_state=42
        ).fit(flat_img_sample)
        center = kmeans_instance.cluster_centers_
        label = kmeans_instance.predict(flat_img)
        nb_colours, nb_colours_under_threshold = update_nb_colours(
            label, nb_pixels, threshold_pixel_percentage, nb_colours  # , flat_img
        )

    return process_result(center, label, img.shape)


def test_sklearn_kmeans2(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_sklearn_iter(img_input, KMeans)


def test_sklearn_mini_batch_kmeans(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_sklearn_iter(img_input, MiniBatchKMeans)


def test_sklearn_mean_shift(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)

    center: np.ndarray
    label: np.ndarray

    flat_img_sample: np.ndarray = sklearn.utils.shuffle(flat_img, random_state=0)[:1000]

    clusterer_instance: MeanShift = MeanShift().fit(flat_img_sample)
    center = clusterer_instance.cluster_centers_
    label = clusterer_instance.predict(flat_img)

    return process_result(center, label, img.shape)


def process_pycluster_result(
    flat_img: np.ndarray,
    clusters: [[int]],
    representatives: [[float]],
    shape: Tuple[int, int, int],
    conversion_method: int = cv2.COLOR_BGR2RGB,
) -> Tuple[Type[Image.Image], np.ndarray]:
    representatives: np.ndarray = np.uint8(representatives)
    for index_cluster, cluster in enumerate(clusters):
        for pixel in cluster:
            flat_img[pixel] = representatives[index_cluster]
    quantized_img: np.ndarray = np.uint8(flat_img.reshape(shape))
    quantized_img = cv2.cvtColor(quantized_img, conversion_method)
    representatives = cv2.cvtColor(
        np.expand_dims(representatives, axis=0), conversion_method
    )[0]
    return Image.fromarray(quantized_img), representatives


def test_pycluster_threshold(
    img_input: Image.Image, func: Callable
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)
    # Prepare algorithm's parameters.
    max_clusters: int = 20
    threshold: float = 15
    # this function gave me the best result with the lest colours
    clusterer: bsas.bsas = func(
        flat_img,
        max_clusters,
        threshold,
        metric=distance_metric(type_metric.CHI_SQUARE),
    )
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: [[float]] = clusterer.get_representatives()
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_bsas(img_input: Image.Image) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_threshold(img_input, bsas.bsas)


def test_pycluster_mbsas(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_threshold(img_input, mbsas.mbsas)


def test_pycluster_neighbours(
    img_input: Image.Image, func: Callable
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)
    # Prepare algorithm's parameters.
    eps: float = 0.7
    neighbors: int = len(flat_img) // 1000
    clusterer: Union[dbscan.dbscan, optics.optics] = func(flat_img, eps, neighbors)
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: np.ndarray = np.asarray(
        [
            np.mean([flat_img[pixel] for pixel in cluster], axis=0)
            for cluster in clusters
        ]
    )
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_dbscan(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_neighbours(img_input, dbscan.dbscan)


def test_pycluster_optics(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_neighbours(img_input, optics.optics)


def test_pycluster_syncnet(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input, True)
    # Prepare algorithm's parameters.
    radius: float = 50

    network: syncnet.syncnet = syncnet.syncnet(flat_img, radius)
    clusterer: syncnet.syncnet_analyser = network.process()
    clusters: [[int]] = clusterer.allocate_clusters()
    representatives: np.ndarray = np.asarray(
        [
            np.mean([flat_img[pixel] for pixel in cluster], axis=0)
            for cluster in clusters
        ]
    )
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_syncsom(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input, True)
    # Prepare algorithm's parameters.
    radius: float = 0.001
    rows: int = 2
    cols: int = 2

    clusterer: syncsom.syncsom = syncsom.syncsom(flat_img, rows, cols, radius)
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: np.ndarray = np.asarray(
        [
            np.mean([flat_img[pixel] for pixel in cluster], axis=0)
            for cluster in clusters
        ]
    )
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_2threshold(
    img_input: Image.Image, func: Callable
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)
    # Prepare algorithm's parameters.
    threshold1: float = 70
    threshold2: float = 120
    # Manhattan, although not particularly good for colour distance, gave me the best results
    clusterer: ttsas.ttsas = func(
        flat_img, threshold1, threshold2, metric=distance_metric(type_metric.MANHATTAN)
    )
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: [[float]] = clusterer.get_representatives()
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_ttsas(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_2threshold(img_input, ttsas.ttsas)


def test_pycluster_xmeans(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)
    amount_initial_centers: int = 2
    initial_centers: [np.ndarray] = center_initializer.kmeans_plusplus_initializer(
        flat_img, amount_initial_centers
    ).initialize()
    max_clusters: int = 20
    clusterer: xmeans.xmeans = xmeans.xmeans(flat_img, initial_centers, max_clusters)
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: [[float]] = clusterer.get_centers()
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_k(
    img_input: Image.Image, func: Callable, center_func_str: str
) -> Tuple[Type[Image.Image], np.ndarray]:
    img, nb_pixels, flat_img = get_img_data(img_input)
    kmin: int = 2
    kmax: int = 20
    elbow_instance: elbow.elbow = elbow.elbow(flat_img, kmin, kmax)
    elbow_instance.process()
    amount_clusters: int = elbow_instance.get_amount()
    centers: [np.ndarray] = center_initializer.kmeans_plusplus_initializer(
        flat_img, amount_clusters
    ).initialize()
    clusterer: Union[kmeans.kmeans, kmedians.kmedians] = func(flat_img, centers)
    clusterer.process()
    clusters: [[int]] = clusterer.get_clusters()
    representatives: [[float]] = eval("clusterer." + center_func_str + "()")
    return process_pycluster_result(flat_img, clusters, representatives, img.shape)


def test_pycluster_kmeans(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_k(img_input, kmeans.kmeans, "get_centers")


def test_pycluster_kmedians(
    img_input: Image.Image
) -> Tuple[Type[Image.Image], np.ndarray]:
    return test_pycluster_k(img_input, kmedians.kmedians, "get_medians")


def create_colour_list_image(
    colours_list: [[int]], img_name: str, quantize_function_name: str
) -> None:
    h, w = (25, 20)
    colour_img: Image.Image = Image.new("RGB", (w * len(colours_list), h))
    colours_list: [Tuple[int, int, int]] = sum(
        [[tuple(colour)] * w for colour in colours_list] * h, []
    )
    colour_img.putdata(colours_list)
    colour_img.save(
        f"./imgs_results/test_colours_{img_name}_{quantize_function_name}.png"
    )


def create_images_results(imgs: [str], quantize_functions: [str]) -> None:
    for img_name in imgs:
        _img: Image.Image = Image.open(f"imgs/{img_name}.jpg")
        for quantize_function_name in quantize_functions:
            func_name = "test_" + quantize_function_name
            quantized_img, colours_list = eval(f"{func_name}(_img)")
            print(
                f"{img_name} - {quantize_function_name} nb colours : {len(colours_list)}"
            )
            quantized_img.save(
                f"./imgs_results/test_img_{img_name}_{quantize_function_name}.png"
            )
            create_colour_list_image(colours_list, img_name, quantize_function_name)


def benchmark(imgs: [str], quantize_functions: [str]) -> None:
    for quantize_function_name in quantize_functions:
        img: Image.Image = Image.open(f"imgs/{imgs[0]}.jpg")
        func_name = "test_" + quantize_function_name
        time = timeit.timeit(
            func_name + "(img)",
            number=10,
            setup="from __main__ import " + func_name,
            globals={"img": img},
        )
        print(f"{quantize_function_name} time : {time} s")


def test_all(imgs: [str], quantize_functions: [str]) -> None:
    create_images_results(imgs, quantize_functions)
    benchmark(imgs, quantize_functions)


if __name__ == "__main__":
    test_all(
        [
            "hanif-mahmad-9aIz3Uz6xsk-unsplash",
            "hanif-mahmad-eEwU2NCrqE8-unsplash",
            "hanif-mahmad-g_Ajr_yG1YA-unsplash",
            "hanif-mahmad-tA_ph2EjJkk-unsplash",
            "hanif-mahmad-Zxjdu-d7vWs-unsplash",
            "simon-launay-0OYeIqq1IC0-unsplash",
            "simon-launay--QC-lCW6yCI-unsplash",
            "simon-launay-a9Sbz8_hW8Q-unsplash",
            "simon-launay-eSlCg_gGNCg-unsplash",
            "simon-launay-Igu6Ig9JthU-unsplash",
            "simon-launay-IgYBZwOVm04-unsplash",
            "simon-launay-lHVpa2WUb9k-unsplash",
            "simon-launay-nYcAQhgpXRk-unsplash",
            "simon-launay-pTaryUjCPkw-unsplash",
            "simon-launay-RIyfkoXxWzc-unsplash",
            "simon-launay-x9WpMb1t2Nc-unsplash",
        ],
        [
            "pillow_median_cut",
            "pillow_maximum_coverage",
            "pillow_fast_octree",
            "opencv_rgb",
            "opencv_hsv",
            "opencv_lab",
            "scipy",
            "scipy2",
            "sklearn_kmeans",
            "sklearn_kmeans2",
            "sklearn_mini_batch_kmeans",
            "sklearn_mean_shift",
            "pycluster_bsas",
            "pycluster_mbsas",
            # "pycluster_dbscan",
            # "pycluster_optics",
            "pycluster_syncnet",
            "pycluster_syncsom",
            "pycluster_ttsas",
            "pycluster_xmeans",
            "pycluster_kmeans",
            "pycluster_kmedians",
        ],
    )
