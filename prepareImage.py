from pathlib import Path
import numpy as np
from scipy import ndimage
from skimage import morphology, measure
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from skimage.transform import resize


def prepareImage(imageName):
    # filename = Path(f'data/images/imgs_part_1/{imageName}')  # PAT_8_15_820.png
    im = plt.imread(imageName)
    im2 = im[0:1500, :, :3]  # Select only the first three channels (RGB)
    im2 = rgb2gray(im2)*256
    im = resize(im, (im.shape[0] // 4, im.shape[1] // 4), anti_aliasing=True)
    return im2


def refineImage(im2, filename):
    thresh = measure_root_mass(filename)
    mask = im2 < thresh  # Value selected by looking at the histogram
    plt.imshow(mask, cmap='gray')
    # Remove small white regions and keep only the largest connected region
    mask = morphology.remove_small_objects(mask, min_size=1000)
    mask = morphology.remove_small_holes(mask, area_threshold=1000)
    mask_largest = morphology.label(mask, connectivity=2)
    props = measure.regionprops(mask_largest)
    if len(props) > 0:
        props.sort(key=lambda x: x.area, reverse=True)
        mask = mask_largest == props[0].label
        # Fill the largest hole inside the mask
        mask = ndimage.binary_fill_holes(mask)
        # Structural element, that we will use as a "brush". The parameter is "brush side"
        struct_el = morphology.disk(6)
        # Use this "brush" to erode and then dilate the image to remove small white regions outside the lesion
        mask = morphology.binary_erosion(mask, struct_el)
        mask = morphology.binary_dilation(mask, struct_el)
    else:
        # If there are no labeled regions, create a blank mask of the same shape as the input image
        mask = np.zeros_like(im2)
    return mask
