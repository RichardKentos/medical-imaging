#import cv2
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import skimage.filters as filters
from skimage import io, measure
from prepareImage import *
from testthreshold import *

# Prepare an image
filename = 'data/images/imgs_part_1/PAT_53_82_940.png'
im2 = prepareImage(filename)
plt.imshow(im2)
plt.show()
gray = refineImage(im2, filename)
plt.imshow(gray)
plt.show()

# Threshold the image to segment the lesion
thresh = measure_root_mass(filename)/255
#thresh = filters.threshold_otsu(gray)
mask = gray > thresh

# Label the connected regions in the mask
labels = measure.label(mask)

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
symmetry_ratio = left_mean_distance / right_mean_distance

# If the ratio is close to 1, the lesion is symmetric
if 0.9 <= symmetry_ratio <= 1.1:
    print('The lesion is symmetric')
else:
    print('The lesion is asymmetric')

# Display the image and mask
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].imshow(gray, cmap='gray')
axes[1].imshow(mask, cmap='gray')
axes[0].set_title('Original Image')
axes[1].set_title('Mask')
fig.tight_layout()
plt.show()
