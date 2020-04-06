![quantize demo cover](imgs_results/quantize_cover.png)
# Quantize Image Methods

Here you'll find different methods to quantize images in Python using clusterisation. Choose your favorite!

All of the functions used are not minimal examples of the different library's method they are using, the time measurements should be looked at with caution and only in the context of image quantization.

All time measurements where taken for 10 successive iterations of a method. Unless otherwise specified, the licenses of the used libraries are freely available for commercial use.
The code used to reproduce all results is available in this [file](demo_quantize_methods.py).

For the photos used for the tests, I tried to select sufficiently diverse ones to really show the specificity to be expected for each methods.
The authors of the photos are [Hanif Mahmad](https://unsplash.com/@anif) (for the first 5) and [Simon Launay](https://unsplash.com/@simonlaunay) (for the rest).

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![building](imgs/hanif-mahmad-9aIz3Uz6xsk-unsplash.jpg) | ![city sunset](imgs/hanif-mahmad-eEwU2NCrqE8-unsplash.jpg) | ![forest panorama](imgs/hanif-mahmad-g_Ajr_yG1YA-unsplash.jpg) | ![mini old lighthouse](imgs/hanif-mahmad-tA_ph2EjJkk-unsplash.jpg)
![red chair](imgs/hanif-mahmad-Zxjdu-d7vWs-unsplash.jpg) | ![walking monks](imgs/simon-launay-0OYeIqq1IC0-unsplash.jpg) | ![coloured tiles painting](imgs/simon-launay--QC-lCW6yCI-unsplash.jpg) | ![busy Japan street](imgs/simon-launay-a9Sbz8_hW8Q-unsplash.jpg)
![cycling woman](imgs/simon-launay-eSlCg_gGNCg-unsplash.jpg) | ![child portrait](imgs/simon-launay-Igu6Ig9JthU-unsplash.jpg) | ![dark tunnel](imgs/simon-launay-IgYBZwOVm04-unsplash.jpg) | ![man in train window](imgs/simon-launay-lHVpa2WUb9k-unsplash.jpg)
![desert road](imgs/simon-launay-nYcAQhgpXRk-unsplash.jpg) | ![tree flower closeup](imgs/simon-launay-pTaryUjCPkw-unsplash.jpg) | ![children playground](imgs/simon-launay-RIyfkoXxWzc-unsplash.jpg) | ![girl portrait](imgs/simon-launay-x9WpMb1t2Nc-unsplash.jpg)

The images where all reduced to a maximum size of 500px (width or height) before quantization (included in time measurement), except specified ones which needed an even smaller size to get back any kind of result.
And without further ado, here are the results:

## Pillow
[Pillow](https://pillow.readthedocs.io/en/stable/) is a rework of the PIL imaging library ; it is the only one of the contestants containing a function dedicated to quantizing.
The function takes a `method` parameter which can be any one of the following quantizing methods: median cut, maximum coverage, fast octree or the custom algorithm of [libimagequant](https://pngquant.org/lib/), 
but this one is an external, either GPL or commercial dependency, and to be able to use it you need to rebuild Pillow yourself while including it ; I didn't test it.
Pillow's quantize method require the precise number of colours that you want in the resulting image.
What I did to choose that number was to iterate over the quantize method, reducing the number of colours until there was none left covering less that 5% of the image.
Although the quantization is applied several times, the method is stilll the quickest by far, as you'll see next.
It is also the only method not using the `cv2.resize` to reduce the image size ; instead it uses Pillow's `Image.thumbnail`.

### Median cut

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pillow_median_cut image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_median_cut.png) | ![pillow_median_cut image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_median_cut.png) | ![pillow_median_cut image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_median_cut.png) | ![pillow_median_cut image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_median_cut.png)
![pillow_median_cut colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_median_cut.png)
![pillow_median_cut image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_median_cut.png) | ![pillow_median_cut image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pillow_median_cut.png) | ![pillow_median_cut image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pillow_median_cut.png) | ![pillow_median_cut image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_median_cut.png)
![pillow_median_cut colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_median_cut.png)
![pillow_median_cut image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pillow_median_cut.png) | ![pillow_median_cut image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pillow_median_cut.png) | ![pillow_median_cut image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pillow_median_cut.png) | ![pillow_median_cut image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pillow_median_cut.png)
![pillow_median_cut colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pillow_median_cut.png)
![pillow_median_cut image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pillow_median_cut.png) | ![pillow_median_cut image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pillow_median_cut.png) | ![pillow_median_cut image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pillow_median_cut.png) | ![pillow_median_cut image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pillow_median_cut.png)
![pillow_median_cut colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pillow_median_cut.png) | ![pillow_median_cut colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pillow_median_cut.png)

pillow_median_cut time : 2.677708653 s

The results are not bad, but you lose vivid colours that are not covering a lot of the image, like the monks' clothing or the road yellow line.

### Maximum coverage

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pillow_maximum_coverage image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pillow_maximum_coverage.png)
![pillow_maximum_coverage colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pillow_maximum_coverage.png) | ![pillow_maximum_coverage colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pillow_maximum_coverage.png)

pillow_maximum_coverage time : 1.9332736510000004 s

This method gives really interesting results. Objects are identifiable but some colours are really transformed and the number of colour might be to small for some.
The advantage is that you get no colour resembling each other in the colours extraction

### Fast octree

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pillow_fast_octree image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_fast_octree.png)
![pillow_fast_octree colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pillow_fast_octree.png)
![pillow_fast_octree image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_fast_octree.png)
![pillow_fast_octree colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pillow_fast_octree.png)
![pillow_fast_octree image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pillow_fast_octree.png)
![pillow_fast_octree colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pillow_fast_octree.png)
![pillow_fast_octree image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pillow_fast_octree.png)
![pillow_fast_octree colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pillow_fast_octree.png) | ![pillow_fast_octree colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pillow_fast_octree.png)

pillow_fast_octree time : 0.47265442100000143 s

This method is by far the fastest one, but the results are really noisy and you lose a lot of vivid colours, even more than with Median cut.

## OpenCV
[OpenCV](https://opencv.org/) is a famous library containing utility functions for computer vision.
For these next set of functions, we are using the `cv2.kmeans` because the quantization problem can be in fact redefined as a clusterisation problem.
Three colour space will be tested, to see if we get better results in colour space where classic distance computation should have a better meaning.
Like the Pillow methods, the function is iterated until we get only colours that are sufficiently present in the image.
The threshold is 1% instead of 5% here, because we didn't get enough colours otherwise.

### RGB

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![opencv_rgb image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_rgb.png) | ![opencv_rgb image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_rgb.png) | ![opencv_rgb image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_rgb.png) | ![opencv_rgb image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_rgb.png)
![opencv_rgb colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_rgb.png) | ![opencv_rgb colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_rgb.png) | ![opencv_rgb colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_rgb.png) | ![opencv_rgb colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_rgb.png)
![opencv_rgb image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_rgb.png) | ![opencv_rgb image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_opencv_rgb.png) | ![opencv_rgb image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_opencv_rgb.png) | ![opencv_rgb image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_rgb.png)
![opencv_rgb colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_rgb.png) | ![opencv_rgb colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_opencv_rgb.png) | ![opencv_rgb colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_opencv_rgb.png) | ![opencv_rgb colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_rgb.png)
![opencv_rgb image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_opencv_rgb.png) | ![opencv_rgb image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_opencv_rgb.png) | ![opencv_rgb image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_opencv_rgb.png) | ![opencv_rgb image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_opencv_rgb.png)
![opencv_rgb colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_opencv_rgb.png) | ![opencv_rgb colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_opencv_rgb.png) | ![opencv_rgb colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_opencv_rgb.png) | ![opencv_rgb colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_opencv_rgb.png)
![opencv_rgb image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_opencv_rgb.png) | ![opencv_rgb image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_opencv_rgb.png) | ![opencv_rgb image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_opencv_rgb.png) | ![opencv_rgb image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_opencv_rgb.png)
![opencv_rgb colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_opencv_rgb.png) | ![opencv_rgb colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_opencv_rgb.png) | ![opencv_rgb colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_opencv_rgb.png) | ![opencv_rgb colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_opencv_rgb.png)

opencv_rgb time : 32.54811209199988 s

Results are really good, the kmeans does really well at extracting the most important colours.
The default is that the time taken took a big leap for the worst compared to Pillow's methods.

### HSV

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![opencv_hsv image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_hsv.png) | ![opencv_hsv image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_hsv.png) | ![opencv_hsv image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_hsv.png) | ![opencv_hsv image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_hsv.png)
![opencv_hsv colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_hsv.png) | ![opencv_hsv colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_hsv.png) | ![opencv_hsv colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_hsv.png) | ![opencv_hsv colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_hsv.png)
![opencv_hsv image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_hsv.png) | ![opencv_hsv image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_opencv_hsv.png) | ![opencv_hsv image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_opencv_hsv.png) | ![opencv_hsv image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_hsv.png)
![opencv_hsv colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_hsv.png) | ![opencv_hsv colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_opencv_hsv.png) | ![opencv_hsv colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_opencv_hsv.png) | ![opencv_hsv colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_hsv.png)
![opencv_hsv image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_opencv_hsv.png) | ![opencv_hsv image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_opencv_hsv.png) | ![opencv_hsv image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_opencv_hsv.png) | ![opencv_hsv image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_opencv_hsv.png)
![opencv_hsv colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_opencv_hsv.png) | ![opencv_hsv colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_opencv_hsv.png) | ![opencv_hsv colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_opencv_hsv.png) | ![opencv_hsv colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_opencv_hsv.png)
![opencv_hsv image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_opencv_hsv.png) | ![opencv_hsv image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_opencv_hsv.png) | ![opencv_hsv image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_opencv_hsv.png) | ![opencv_hsv image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_opencv_hsv.png)
![opencv_hsv colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_opencv_hsv.png) | ![opencv_hsv colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_opencv_hsv.png) | ![opencv_hsv colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_opencv_hsv.png) | ![opencv_hsv colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_opencv_hsv.png)

opencv_hsv time : 50.326093940999954 s

Since HSV is not really supposed to be a good fit for colour distancing, I expected much worse results.
Some colours have a wrong hue, but overall it's not that bad.
RGB is still more faithful and take less time, so you shouldn't use HSV.

### LAB

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![opencv_lab image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_lab.png) | ![opencv_lab image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_lab.png) | ![opencv_lab image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_lab.png) | ![opencv_lab image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_lab.png)
![opencv_lab colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_opencv_lab.png) | ![opencv_lab colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_opencv_lab.png) | ![opencv_lab colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_opencv_lab.png) | ![opencv_lab colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_opencv_lab.png)
![opencv_lab image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_lab.png) | ![opencv_lab image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_opencv_lab.png) | ![opencv_lab image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_opencv_lab.png) | ![opencv_lab image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_lab.png)
![opencv_lab colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_opencv_lab.png) | ![opencv_lab colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_opencv_lab.png) | ![opencv_lab colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_opencv_lab.png) | ![opencv_lab colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_opencv_lab.png)
![opencv_lab image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_opencv_lab.png) | ![opencv_lab image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_opencv_lab.png) | ![opencv_lab image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_opencv_lab.png) | ![opencv_lab image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_opencv_lab.png)
![opencv_lab colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_opencv_lab.png) | ![opencv_lab colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_opencv_lab.png) | ![opencv_lab colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_opencv_lab.png) | ![opencv_lab colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_opencv_lab.png)
![opencv_lab image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_opencv_lab.png) | ![opencv_lab image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_opencv_lab.png) | ![opencv_lab image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_opencv_lab.png) | ![opencv_lab image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_opencv_lab.png)
![opencv_lab colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_opencv_lab.png) | ![opencv_lab colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_opencv_lab.png) | ![opencv_lab colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_opencv_lab.png) | ![opencv_lab colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_opencv_lab.png)

opencv_lab time : 34.00670318699986 s

Lab should theoretically give better result than RGB, being a colour space created to give better distance measurement.
But the RGB already gives good results, and I don't see any visible improvement by using Lab.
Time taken also is similar, so you can probably use either one.
You should theoretically get better results by using Delta E 2000 instead of euclidian distance, but openCV doesn't give us the possibility to change the distance function.
Based upon these results, all following methods will use RGB colour space.

## SciPy

[SciPy](https://www.scipy.org/) is a library for scientific computing. Like OpenCV, it contains a function for KMeans, and that's what I used.
Unlike OpenCV, the function can be divided in two parts: the first find the centroids (fit), the second create the pixel clusters using those (predict).
The threshold of the minimum colour presence percentage was set at 2% which produced not too much nor too little colours.

### Without optimisation trick

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![scipy image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_scipy.png) | ![scipy image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_scipy.png) | ![scipy image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_scipy.png) | ![scipy image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_scipy.png)
![scipy colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_scipy.png) | ![scipy colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_scipy.png) | ![scipy colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_scipy.png) | ![scipy colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_scipy.png)
![scipy image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_scipy.png) | ![scipy image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_scipy.png) | ![scipy image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_scipy.png) | ![scipy image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_scipy.png)
![scipy colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_scipy.png) | ![scipy colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_scipy.png) | ![scipy colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_scipy.png) | ![scipy colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_scipy.png)
![scipy image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_scipy.png) | ![scipy image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_scipy.png) | ![scipy image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_scipy.png) | ![scipy image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_scipy.png)
![scipy colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_scipy.png) | ![scipy colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_scipy.png) | ![scipy colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_scipy.png) | ![scipy colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_scipy.png)
![scipy image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_scipy.png) | ![scipy image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_scipy.png) | ![scipy image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_scipy.png) | ![scipy image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_scipy.png)
![scipy colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_scipy.png) | ![scipy colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_scipy.png) | ![scipy colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_scipy.png) | ![scipy colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_scipy.png)

scipy time : 524.6095604020002 s

We can see that the result is similar to those of the Median cut of Pillow: you lose some vivid minority colours.
But the main problem is the time ; using a threshold of 2% instead of 1%, I expected the function to take more time than the OpenCV equivalent.
But this is just ridiculous and unusable.
Fortunately, what you'll see next is a trick to get similar results in much less time.

### With optimisation trick

Since the quantization is done in two steps, we can compute the centroids on a randomized shuffle subset of the original image, and then apply the model to the whole image.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![scipy2 image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_scipy2.png) | ![scipy2 image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_scipy2.png) | ![scipy2 image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_scipy2.png) | ![scipy2 image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_scipy2.png)
![scipy2 colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_scipy2.png) | ![scipy2 colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_scipy2.png) | ![scipy2 colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_scipy2.png) | ![scipy2 colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_scipy2.png)
![scipy2 image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_scipy2.png) | ![scipy2 image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_scipy2.png) | ![scipy2 image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_scipy2.png) | ![scipy2 image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_scipy2.png)
![scipy2 colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_scipy2.png) | ![scipy2 colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_scipy2.png) | ![scipy2 colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_scipy2.png) | ![scipy2 colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_scipy2.png)
![scipy2 image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_scipy2.png) | ![scipy2 image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_scipy2.png) | ![scipy2 image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_scipy2.png) | ![scipy2 image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_scipy2.png)
![scipy2 colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_scipy2.png) | ![scipy2 colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_scipy2.png) | ![scipy2 colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_scipy2.png) | ![scipy2 colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_scipy2.png)
![scipy2 image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_scipy2.png) | ![scipy2 image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_scipy2.png) | ![scipy2 image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_scipy2.png) | ![scipy2 image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_scipy2.png)
![scipy2 colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_scipy2.png) | ![scipy2 colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_scipy2.png) | ![scipy2 colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_scipy2.png) | ![scipy2 colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_scipy2.png)

scipy2 time : 6.44186058299988 s

As you can see, the results are pretty much the same as those without optimisation, for a much more reasonable computation time, even much better than OpenCV.

## Scikit-learn

[Scikit-learn](https://scikit-learn.org/stable/) is specialised in machine learning tools (classification, regression and clustering).
We will use KMeans with same parameters and process as those used with SciPy, and we will try some other clusterisation functions available.

### KMeans without optimisation trick

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![sklearn_kmean image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_kmean.png) | ![sklearn_kmean image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_kmean.png) | ![sklearn_kmean image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_kmean.png) | ![sklearn_kmean image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_kmean.png)
![sklearn_kmean colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_kmean.png)
![sklearn_kmean image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_kmean.png) | ![sklearn_kmean image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_sklearn_kmean.png) | ![sklearn_kmean image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_sklearn_kmean.png) | ![sklearn_kmean image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_kmean.png)
![sklearn_kmean colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_kmean.png)
![sklearn_kmean image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_sklearn_kmean.png) | ![sklearn_kmean image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_sklearn_kmean.png) | ![sklearn_kmean image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_sklearn_kmean.png) | ![sklearn_kmean image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_sklearn_kmean.png)
![sklearn_kmean colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_sklearn_kmean.png)
![sklearn_kmean image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_sklearn_kmean.png) | ![sklearn_kmean image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_sklearn_kmean.png) | ![sklearn_kmean image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_sklearn_kmean.png) | ![sklearn_kmean image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_kmean.png)
![sklearn_kmean colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_sklearn_kmean.png) | ![sklearn_kmean colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_kmean.png)

sklearn_kmeans time : 292.4821637319999 s

The time is once again ridiculously long, but since we can use the same trick as with Scipy, let's see the results with it.

### KMeans with optimisation trick

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![sklearn_kmean2 image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_kmean2.png)
![sklearn_kmean2 colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_sklearn_kmean2.png) | ![sklearn_kmean2 colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_kmean2.png)

sklearn_kmean2 time : 7.649859192999884 s

Like SciPy, we managed to have similar result for a much better time.
Unfortunately, there is one image, the road one, where the result of the quantization is actually visibly worse by using the optimisation, but such case should be rare.

### MiniBatchKMeans

MiniBatchKMeans is a variant of KMeans meant to take less computation time for a similar result.
Since we have already seen that quantizing on a random sample works relatively well, this function directly use the optimised version.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![sklearn_mini_batch_kmeans image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_mini_batch_kmeans.png)
![sklearn_mini_batch_kmeans colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_sklearn_mini_batch_kmeans.png) | ![sklearn_mini_batch_kmeans colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_mini_batch_kmeans.png)

sklearn_mini_batch_kmeans time : 74.64295504700002 s

Contrarily to what is promised, we actually have worse time performance by using MiniBatchKMeans rather than KMeans, even though the rest of the implementation of the function is exactly the same.
Aside from that, the images result are similar, and even better for a few, to those of KMeans.

### MeanShift

MeanShift tries to discover "blobs" of data, and in a second step regroups together blobs that are near-duplicates.
Because of its implementation, there is no need to give this method the number of colours we want, it will chose it.
Since this method can be done in two steps (fit then predict), we will once again use a random sample for the fitting to reduce computation time.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![sklearn_mean_shift image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_mean_shift.png)
![sklearn_mean_shift colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_sklearn_mean_shift.png) | ![sklearn_mean_shift colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_sklearn_mean_shift.png)

sklearn_mean_shift time : 52.089231103 s

The resulting images are quite good, even if a lot of them are a bit to minimalistic in colours (except for the tunnel one which is surprisingly and uselessly detailed).
Time taken is quite long however.

## Pyclustering

[Pyclustering](https://pyclustering.github.io/), like its name implies, is specialised in clusterisation, but it uses a GPL license.
With it we are able to test several different cluster functions aside from K-Means.
CCORE included library is used to get better performances.

### BSAS

BSAS use a maximum allowable number of clusters and a threshold of dissimilarity as parameters, as well as the distance function to be used.
The number of clusters is then decided by the algorithm, and we don't need to loop and check pixel percentage coverage ourselves.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_bsas image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_bsas.png) | ![pycluster_bsas image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_bsas.png) | ![pycluster_bsas image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_bsas.png) | ![pycluster_bsas image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_bsas.png)
![pycluster_bsas colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_bsas.png)
![pycluster_bsas image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_bsas.png) | ![pycluster_bsas image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_bsas.png) | ![pycluster_bsas image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_bsas.png) | ![pycluster_bsas image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_bsas.png)
![pycluster_bsas colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_bsas.png)
![pycluster_bsas image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_bsas.png) | ![pycluster_bsas image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_bsas.png) | ![pycluster_bsas image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_bsas.png) | ![pycluster_bsas image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_bsas.png)
![pycluster_bsas colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_bsas.png)
![pycluster_bsas image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_bsas.png) | ![pycluster_bsas image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_bsas.png) | ![pycluster_bsas image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_bsas.png) | ![pycluster_bsas image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_bsas.png)
![pycluster_bsas colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_bsas.png) | ![pycluster_bsas colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_bsas.png)

pycluster_bsas time : 33.03888442999994 s

The results are interesting, but clearly not adapted for colour quantization.
Some images are deformed, hardly recognisable, and some colours are not even the hue they should be.
Time taken is equivalent to OpenCV.

### MBSAS

MBSAS is similar to BSAS but for some implementation details I won't get into here.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_mbsas image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_mbsas.png)
![pycluster_mbsas colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_mbsas.png)
![pycluster_mbsas image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_mbsas.png)
![pycluster_mbsas colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_mbsas.png)
![pycluster_mbsas image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_mbsas.png)
![pycluster_mbsas colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_mbsas.png)
![pycluster_mbsas image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_mbsas.png)
![pycluster_mbsas colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_mbsas.png) | ![pycluster_mbsas colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_mbsas.png)

pycluster_mbsas time : 33.16758375900008 s

As expected, image and time results are comparable to those of BSAS.

### DBSCAN

|               |
|:-------------:|
|![pycluster_dbscan image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_dbscan.png)|
|![pycluster_dbscan colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_dbscan.png)|

pycluster_dbscan time : 102.73210900899994 s

With DBSCAN, not all pixel are guaranteed to be in a cluster, some samples are considered noisy and not included in a cluster.
In an image, you can't just decide a pixel is an outsider and not assign it to a cluster since it needs to have a colour.
Therefore you need a lot of clusters to be certain there will be no outsider.
Hence why I didn't test this algorithm on all the photos: as well as taking a lot of time, it is clearly not suitable for the quantization problem.

### OPTICS

|               |
|:-------------:|
|![pycluster_optics image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_optics.png)|
|![pycluster_optics colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_optics.png)|

pycluster_optics time : 122.5359561910002 s

OPTICS give similar results as those of DBSCAN which is expected since OPTICS is actually a lower memory consumption alternative to DBSCAN.
That's why we also didn't test sklearn.cluster.DBSCAN and sklearn.cluster.OPTICS: they would also gives outsiders.

### SyncNet
SyncNEt construct an oscillatory network to do clusterisation.
Because of that, it was impossible to use without greatly reducing the size of the image first: 83px maximum (function crashed on my machine on the original 500px maximum size).

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_syncnet image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_syncnet.png)
![pycluster_syncnet colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_syncnet.png)
![pycluster_syncnet image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_syncnet.png)
![pycluster_syncnet colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_syncnet.png)
![pycluster_syncnet image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_syncnet.png)
![pycluster_syncnet colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_syncnet.png)
![pycluster_syncnet image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_syncnet.png)
![pycluster_syncnet colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_syncnet.png) | ![pycluster_syncnet colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_syncnet.png)

pycluster_syncnet time : 334.00758747099985 s

The results are pretty poor, the number of selected colours fluctuates a lot between images and the time taken is much too high event though the image is 6 times smaller than those of the other methods.
This algorithm can't be used for quantization.

### SYNC-SOM

SYNC-SOM works similarly to SyncNet, with the same problem of needing small images to even function.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_syncsom image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_syncsom.png)
![pycluster_syncsom colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_syncsom.png)
![pycluster_syncsom image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_syncsom.png)
![pycluster_syncsom colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_syncsom.png)
![pycluster_syncsom image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_syncsom.png)
![pycluster_syncsom colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_syncsom.png)
![pycluster_syncsom image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_syncsom.png)
![pycluster_syncsom colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_syncsom.png) | ![pycluster_syncsom colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_syncsom.png)

pycluster_syncsom time : 1103.5881241590002 s

The results are comparable to those of SyncNet while taking an even greater time to be computed.
This algorithm can't be used for quantization.

### TTSAS

TTSAS is an alternative to BSAS and MBSAS that uses two thresholds instead of one.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_ttsas image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_ttsas.png)
![pycluster_ttsas colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_ttsas.png)
![pycluster_ttsas image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_ttsas.png)
![pycluster_ttsas colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_ttsas.png)
![pycluster_ttsas image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_ttsas.png)
![pycluster_ttsas colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_ttsas.png)
![pycluster_ttsas image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_ttsas.png)
![pycluster_ttsas colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_ttsas.png) | ![pycluster_ttsas colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_ttsas.png)

pycluster_ttsas time : 32.75301202599985 s

One again, the result is similar to BSAS, and not adapted to image quantization.

### X-Means

X-Means works by giving it the minimum and maximum number of clusters you want and then dynamically grow from the minimum number until the result is satisfying.
I put the minimum at 2 clusters because that's the limit for an image not to be blank.
You also need to give the method the cluster centers starting position, but pyclustering possess a function, `kmeans_plusplus_initializer`, to initialise the given number of centers at good starting positions for this family of algorithms.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_xmeans image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_xmeans.png)
![pycluster_xmeans colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_xmeans.png)
![pycluster_xmeans image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_xmeans.png)
![pycluster_xmeans colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_xmeans.png)
![pycluster_xmeans image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_xmeans.png)
![pycluster_xmeans colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_xmeans.png)
![pycluster_xmeans image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_xmeans.png)
![pycluster_xmeans colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_xmeans.png) | ![pycluster_xmeans colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_xmeans.png)

pycluster_xmeans time : 61.51795905300014 s

Results are quite good, but the algorithm has a tendency to use the maximum number of colours, even on images where you would expect a very low number of colours to be needed, like the tunnel photo.
Time taken is twice that of OpenCV's KMeans.

### K-Means

Like X-Means, you need to give it the starting centers, for which you can use `kmeans_plusplus_initializer`.
Since pyclustering is slower than openCV and has more utility functions for clusterisation, instead of iterating to find a good number of clusters for each image, we use the Elbow Method to choose for us the optimal number of clusters for each image.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_kmeans image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_kmeans.png)
![pycluster_kmeans colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_kmeans.png)
![pycluster_kmeans image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_kmeans.png)
![pycluster_kmeans colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_kmeans.png)
![pycluster_kmeans image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_kmeans.png)
![pycluster_kmeans colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_kmeans.png)
![pycluster_kmeans image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_kmeans.png)
![pycluster_kmeans colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_kmeans.png) | ![pycluster_kmeans colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_kmeans.png)

pycluster_kmeans time : 150.11819599299997 s

I think the images results are clearly the best ones we got yet, the Elbow Method is clearly efficient at choosing the appropriate number of colours.
The only image where it seems to be missing some colours is the chair one.
But the time taken is unfortunately quite high.

### K-Medians

K-Medians is similar to K-Means except that it compute medians instead of centroid, making it less vulnerable to outliers.

|               |               |               |               |
|:-------------:|:-------------:|:-------------:|:-------------:|
![pycluster_kmedians image building](imgs_results/test_img_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image city sunset](imgs_results/test_img_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image forest panorama](imgs_results/test_img_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image mini old lighthouse](imgs_results/test_img_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_kmedians.png)
![pycluster_kmedians colours building](imgs_results/test_colours_hanif-mahmad-9aIz3Uz6xsk-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours city sunset](imgs_results/test_colours_hanif-mahmad-eEwU2NCrqE8-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours forest panorama](imgs_results/test_colours_hanif-mahmad-g_Ajr_yG1YA-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours mini old lighthouse](imgs_results/test_colours_hanif-mahmad-tA_ph2EjJkk-unsplash_pycluster_kmedians.png)
![pycluster_kmedians image red chair](imgs_results/test_img_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image walking monks](imgs_results/test_img_simon-launay-0OYeIqq1IC0-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image coloured tiles painting](imgs_results/test_img_simon-launay--QC-lCW6yCI-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image busy Japan street](imgs_results/test_img_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_kmedians.png)
![pycluster_kmedians colours red chair](imgs_results/test_colours_hanif-mahmad-Zxjdu-d7vWs-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours walking monks](imgs_results/test_colours_simon-launay-0OYeIqq1IC0-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours coloured tiles painting](imgs_results/test_colours_simon-launay--QC-lCW6yCI-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours busy Japan street](imgs_results/test_colours_simon-launay-a9Sbz8_hW8Q-unsplash_pycluster_kmedians.png)
![pycluster_kmedians image cycling woman](imgs_results/test_img_simon-launay-eSlCg_gGNCg-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image child portrait](imgs_results/test_img_simon-launay-Igu6Ig9JthU-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image dark tunnel](imgs_results/test_img_simon-launay-IgYBZwOVm04-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image man in train window](imgs_results/test_img_simon-launay-lHVpa2WUb9k-unsplash_pycluster_kmedians.png)
![pycluster_kmedians colours cycling woman](imgs_results/test_colours_simon-launay-eSlCg_gGNCg-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours child portrait](imgs_results/test_colours_simon-launay-Igu6Ig9JthU-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours dark tunnel](imgs_results/test_colours_simon-launay-IgYBZwOVm04-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours man in train window](imgs_results/test_colours_simon-launay-lHVpa2WUb9k-unsplash_pycluster_kmedians.png)
![pycluster_kmedians image desert road](imgs_results/test_img_simon-launay-nYcAQhgpXRk-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image tree flower closeup](imgs_results/test_img_simon-launay-pTaryUjCPkw-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image children playground](imgs_results/test_img_simon-launay-RIyfkoXxWzc-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians image girl portrait](imgs_results/test_img_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_kmedians.png)
![pycluster_kmedians colours desert road](imgs_results/test_colours_simon-launay-nYcAQhgpXRk-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours tree flower closeup](imgs_results/test_colours_simon-launay-pTaryUjCPkw-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours children playground](imgs_results/test_colours_simon-launay-RIyfkoXxWzc-unsplash_pycluster_kmedians.png) | ![pycluster_kmedians colours girl portrait](imgs_results/test_colours_simon-launay-x9WpMb1t2Nc-unsplash_pycluster_kmedians.png)

pycluster_kmedians time : 188.61640517599972 s

The results are both slower and less faithful than K-Means.
It might be because when we look at an image, what our brain is doing is actually a mean of each colour area, hence why the colour seems so different when we take the median instead.


## Conclusion
![benchmarks](imgs_results/benchmarks.png)

Pillow's methods are, by a large margin, the fastest ones. Their image results aren't bad, but they are not the best either.
That prize goes to pyclustering's K-Means. But that function is very slow and, although it can probably be speeded up, the pyclustering library is under GPL, which might make it incompatible for some uses.
You'll need to take a decision depending on what requirements you have.
I hope these samples will help you to reach a decision if you one day need to do image quantization.


### Notes:
- The code used assumes that you are only using RGB images. It will need tweaking to support more image formats, but it won't be hard to do once you've chosen your method.
- I am not a professional benchmarker, but these time results are so far from each other that my naive implementation is probably enough to get an accurate idea of the time difference magnitude.
- The constants used as parameters for the different functions might not be the best ones, theses results were just produced to give me an idea of what to expect.
- This list is of course not exhaustive, don't hesitate to suggest other options to me!
