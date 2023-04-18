import matplotlib.pyplot as plt
import numpy as np
import skimage.filters as filters
import skimage.color as color
from skimage.color import rgb2gray
import skimage.morphology as morphology
from skimage import measure
from scipy import ndimage
from pathlib import Path

# Prepare an image
file_im = Path('data\images\imgs_part_1\PAT_573_1090_660.png') #PAT_8_15_820.png
im = plt.imread(file_im)
im2 = im[0:1500, :, :3]  # Select only the first three channels (RGB)
im2 = rgb2gray(im2)*256
plt.imshow(im2, cmap='gray')

# Can we use the histogram to extract the lesion?
mask = im2 < 95  # Value selected by looking at the histogram
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

# Show the resulting mask next to the original image
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].imshow(im2, cmap='gray')
axes[1].imshow(mask, cmap='gray')
axes[0].set_title('Original Image')
axes[1].set_title('Mask')
fig.tight_layout()
plt.show()
