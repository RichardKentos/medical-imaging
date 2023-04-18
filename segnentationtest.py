import numpy as np
import matplotlib.pyplot as plt
from skimage import io, measure
from scipy.spatial.distance import cdist

# Load the image
image = io.imread('data/images/guide_images/PAT_89_135_11.png')

# Label the connected regions in the mask
labels = measure.label(image)

# Find the largest connected region, which is assumed to be the lesion
props = measure.regionprops(labels)
largest_region = props[0]
for region in props:
    if region.area > largest_region.area:
        largest_region = region

# Get the coordinates of the boundary points of the lesion
coords = largest_region.coords

# Find the centroid of the lesion
centroid = largest_region.centroid

# Divide the lesion into left and right halves based on the centroid
left_half = coords[coords[:, 1] < centroid[1]]
right_half = coords[coords[:, 1] >= centroid[1]]

# Compute the Euclidean distance between each pair of boundary points
left_distances = cdist(left_half, left_half)
right_distances = cdist(right_half, right_half)

# Compute the mean distance between boundary points for each half
left_mean_distance = np.mean(left_distances)
right_mean_distance = np.mean(right_distances)

# Compute the ratio of the mean distances between the left and right halves
if left_mean_distance <= right_mean_distance:
    symmetry_ratio = left_mean_distance / right_mean_distance
else:
    symmetry_ratio = right_mean_distance / left_mean_distance

# If the ratio is close to 1, the lesion is symmetric
if 0.9 <= symmetry_ratio <= 1.1:
    print('The lesion is symmetric')
else:
    print('The lesion is asymmetric')
