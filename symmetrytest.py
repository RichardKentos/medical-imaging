from skimage import transform
import matplotlib.pyplot as plt
import numpy as np
from main import *
from prepareImage import *

imgname = 'data/images/imgs_part_1/PAT_585_1130_552.png'
# imgname = 'data/images/TestImagesPart2/ball.png'


def getSymmetry(filename):
    distances = []
    for angle in range(0, 180, 10):
        segmented = mainfunction(filename)
        rot_im = transform.rotate(segmented, angle)
        # How many 1's in each column of the image (sum over axis 0, i.e. rows)
        pixels_in_col = np.sum(rot_im, axis=0)
        # Without this there are some non zeros and ones still because of the resizing
        pixels2 = pixels_in_col > 0
        pixels2 = pixels2.astype(np.int8)
        diameter = np.max(pixels_in_col)
        distances.append(diameter)
    return max(distances) - min(distances)


print(getSymmetry(imgname))
