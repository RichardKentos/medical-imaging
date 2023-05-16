import numpy as np

from imagesegmentation import segmentImage
from prepareImage import *


def getDiameter(filename):
    segmented = segmentImage(filename)
    # Measure diameter of the lesion: measure height or width of the mask
    # How many 1's in each column of the image (sum over axis 0, i.e. rows)
    pixels_in_col = np.sum(segmented, axis=0)
    # Without this there are some non zeros and ones still because of the resizing
    pixels2 = pixels_in_col > 0
    pixels2 = pixels2.astype(np.int8)
    diameter = np.max(pixels_in_col)
    return diameter

# print(getDiameter(imgname))
