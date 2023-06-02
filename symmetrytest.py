from skimage import transform
import numpy as np

"""
Calculate the symmetry of a segmented image.

This function calculates the symmetry of a segmented image by rotating it at different angles and analyzing the
distribution of pixels in each column. The difference between the maximum and minimum diameters is returned as a
measure of symmetry.

Args:
    segImage (numpy.ndarray): The segmented image to analyze.

Returns:
    float: The difference between the maximum and minimum diameters, indicating the symmetry of the image.
"""


def getSymmetry(segImage):
    diameters = []
    normalizations = []
    for angle in range(0, 180, 10):
        segmented = segImage
        rot_im = transform.rotate(segmented, angle)
        # How many 1's in each column of the image (sum over axis 0, i.e. rows)
        pixels_in_col = np.sum(rot_im, axis=0)
        # Without this there are some non zeros and ones still because of the resizing
        pixels2 = pixels_in_col > 0
        pixels2 = pixels2.astype(np.int8)
        diameter = np.max(pixels_in_col)
        diameters.append(diameter)
    for diameter in diameters:
        normalized = (diameter - min(diameters)) / \
                     (max(diameters) - min(diameters))
        normalizations.append(normalized)
    difference = max(diameters) - min(diameters)
    return difference
