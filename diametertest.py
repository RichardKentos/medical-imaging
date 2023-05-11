import numpy as np
from prepareImage import *
from main import *


imgname = 'data/images/imgs_part_1/PAT_585_1130_552.png'


def getDiameterTest(filename):
    segmented = mainfunction(filename)
    print(segmented)
    # Measure diameter of the lesion: measure height or width of the mask
    # How many 1's in each column of the image (sum over axis 0, i.e. rows)
    pixels_in_col = np.sum(segmented, axis=0)
    # Without this there are some non zeros and ones still because of the resizing
    pixels2 = pixels_in_col > 0
    pixels2 = pixels2.astype(np.int8)
    diameter = np.max(pixels_in_col)
    return diameter


print(getDiameterTest(imgname))
