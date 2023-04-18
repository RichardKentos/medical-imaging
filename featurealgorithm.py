from skimage import transform
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from pathlib import Path
from skimage.transform import resize
from prepareImage import *

def is_symmetric(matrix):
    """
    Determines if a given binary matrix is symmetric.
    Args:
        matrix (list of lists): A binary matrix.
    Returns:
        bool: True if the matrix is symmetric, False otherwise.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if the number of rows equals the number of columns
    if rows != cols:
        return False

    # Check if the matrix is symmetric
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Prepare an image
filename = 'PAT_72_110_647.png'
im1 = prepareImage(filename)
#plt.imshow(prepareImage(filename), cmap="gray")
im2 = refineImage(im1)
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

#is_symmetric(pixels2)



