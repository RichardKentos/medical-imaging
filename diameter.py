import numpy as np

"""
Measure the diameter of a segmented image.

This function measures the diameter of a segmented image by analyzing the pixel distribution in each column of the
image. The maximum value in the column sums represents the diameter.

Args:
    segImage (numpy.ndarray): The segmented image to measure the diameter of.

Returns:
    int: The diameter of the segmented image.
"""


def getDiameter(segImage):
    segmented = segImage
    # Measure diameter of the lesion: measure height or width of the mask
    # How many 1's in each column of the image (sum over axis 0, i.e. rows)
    pixels_in_col = np.sum(segmented, axis=0)
    # Without this there are some non zeros and ones still because of the resizing
    pixels2 = pixels_in_col > 0
    pixels2 = pixels2.astype(np.int8)
    diameter = np.max(pixels_in_col)
    return diameter
