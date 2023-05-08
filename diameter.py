import numpy as np
from prepareImage import *


filename = 'data/images/imgs_part_1/PAT_585_1130_552.png'


def getDiameter(filename):
    im1 = prepareImage(filename)
    #plt.imshow(prepareImage(filename), cmap="gray")
    mask = refineImage(im1, filename)
    pixels_in_col = np.sum(mask, axis=1)
    pixels2 = pixels_in_col > 0
    pixels2 = pixels2.astype(np.int8)
    # print(pixels2)
    # Find the centroid
    cy, cx = np.where(np.array([pixels2]))
    cx_mean = np.mean(cx)
    cy_mean = np.mean(cy)
    # Calculate the distance of each non-zero pixel from the centroid
    distances = np.sqrt((cx - cx_mean)**2 + (cy - cy_mean)**2)
    print(distances)
    # Find the maximum distance, which gives us the diameter
    diameter = 2 * np.max(distances)
    return diameter


print(getDiameter(filename))
