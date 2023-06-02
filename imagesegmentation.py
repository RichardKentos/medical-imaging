import cv2
import skimage

import numpy as np
from scipy import ndimage
from skimage import morphology, measure
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

"""
Segment an input image using various image processing techniques.

This function loads an image, performs image processing operations such as resizing, grayscale conversion, blurring,
thresholding, and morphological operations to create a binary mask that selects the foreground. The foreground is
then extracted from the original image using the binary mask.

Args:
    filename (str): The path of the image file to segment.

Returns:
    numpy.ndarray: The segmented image where the foreground is selected, and the rest is set to zero.
"""


def segmentImage(filename):
    imgfile = plt.imread(filename)
    imgfile = cv2.resize(imgfile, (512, 512))

    # convert the image to grayscale
    gray_image = skimage.color.rgb2gray(imgfile[..., 0:3])

    # blur the image to denoise
    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

    # perform automatic thresholding
    t = skimage.filters.threshold_otsu(blurred_image)

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

    # apply the binary mask to select the foreground
    selection = imgfile.copy()
    selection[~binary_mask] = 0

    return selection

