from skimage import transform
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from pathlib import Path
from skimage.transform import resize

# Prepare an image
filename = 'PAT_573_1090_660.png'
file_im = Path(f'data/images/imgs_part_1/{filename}')  # PAT_8_15_820.png
im = plt.imread(file_im)
im2 = im[0:1500, :, :3]  # Select only the first three channels (RGB)
im2 = rgb2gray(im2)*256


# Measure diameter of the lesion: measure height or width of the mask

# How many 1's in each column of the image (sum over axis 0, i.e. rows)
pixels_in_col = np.sum(im2, axis=0)
print(im2.shape)
print(pixels_in_col.shape)


# Without this there are some non zeros and ones still because of the resizing
pixels2 = pixels_in_col > 0
pixels2 = pixels2.astype(np.int8)

print(pixels2)

rot_im = transform.rotate(im2, 40)
