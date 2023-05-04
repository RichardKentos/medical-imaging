import numpy as np
from prepareImage import *


filename = 'data/images/imgs_part_1/PAT_585_1130_552.png'
im1 = prepareImage(filename)
#plt.imshow(prepareImage(filename), cmap="gray")
im2 = refineImage(im1, filename)
pixels_in_col = np.sum(im2, axis=1)
pixels2 = pixels_in_col > 0
pixels2 = pixels2.astype(np.int8)
# print(pixels2)

# Find the centroid
cy, cx = np.where(np.array([pixels2]))
cx_mean = np.mean(cx)
cy_mean = np.mean(cy)
print(cx_mean, cy_mean)


# Calculate the distance of each non-zero pixel from the centroid
distances = np.sqrt((cx - cx_mean)**2 + (cy - cy_mean)**2)

# print(distances)


# Find the maximum distance, which gives us the diameter
diameter = 2 * np.max(distances)

print(f"Diameter of the object: {diameter}")
