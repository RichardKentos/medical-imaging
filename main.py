import cv2
import skimage
from pathlib import Path
import numpy as np
from scipy import ndimage
from skimage import morphology, measure
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from skimage.transform import resize
import os
from symmetry import *

folder_dir = "data/images/guide_images"
# for images in os.listdir(folder_dir):
#     # check if the image ends with png
#     if (images.endswith(".png")):
#         print(is_symmetric(f"{folder_dir}/{images}"))


def mainfunction(filename):
    # data/images/imgs_part_1/PAT_53_82_940.pn
    imgfile = plt.imread(filename)
    # data/images/guide_images/PAT_72_110_647.png
    # data/images/guide_images/PAT_577_1107_61.png
    imgfile = cv2.resize(imgfile, (512, 512))

    # fig, ax = plt.subplots()
    # plt.imshow(imgfile)

    # convert the image to grayscale
    gray_image = skimage.color.rgb2gray(imgfile[..., 0:3])

    # blur the image to denoise
    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
    # plt.imshow(blurred_image)
    # plt.show()  # show the blurred image

    # show the histogram of the blurred image
    # histogram, bin_edges = np.histogram(
    #     blurred_image, bins=256, range=(0.0, 1.0))
    # fig, ax = plt.subplots()
    # # plt.plot(bin_edges[0:-1], histogram)
    # plt.title("Graylevel histogram")
    # plt.xlabel("gray value")
    # plt.ylabel("pixel count")
    # plt.xlim(0, 1.0)

    # perform automatic thresholding
    t = skimage.filters.threshold_otsu(blurred_image)
    # x = skimage.filters.try_all_threshold(blurred_image)
    # print(x)

    # print("Found automatic threshold t = {}.".format(t))

    # create a binary mask with the threshold found by Otsu's method
    binary_mask = blurred_image < t

    # reduce noise and clean the image
    binary_mask = morphology.remove_small_objects(binary_mask, min_size=1000)
    binary_mask = morphology.remove_small_holes(
        binary_mask, area_threshold=1000)
    mask_largest = morphology.label(binary_mask, connectivity=2)
    props = measure.regionprops(mask_largest)
    if len(props) > 0:
        props.sort(key=lambda x: x.area, reverse=True)
        binary_mask = mask_largest == props[0].label

        # Fill the largest hole inside the mask
        binary_mask = ndimage.binary_fill_holes(binary_mask)

        # Structural element, that we will use as a "brush". The parameter is "brush side"
        struct_el = morphology.disk(6)

        # Use this "brush" to erode and then dilate the image to remove small white regions outside the lesion
        binary_mask = morphology.binary_erosion(binary_mask, struct_el)
        binary_mask = morphology.binary_dilation(binary_mask, struct_el)
    else:
        # If there are no labeled regions, create a blank mask of the same shape as the input image
        binary_mask = np.zeros_like(blurred_image, dtype='uint8')

    # fig, ax = plt.subplots()
    # plt.imshow(binary_mask, cmap="gray")  # show the black/white segmentation

    # apply the binary mask to select the foreground
    selection = imgfile.copy()
    selection[~binary_mask] = 0

    # fig, ax = plt.subplots()
    # plt.imshow(selection)
    # plt.show()  # show the segmented lesion
    return selection
plt.imshow(mainfunction("data/images/guide_images/PAT_72_110_647.png"))
plt.show()