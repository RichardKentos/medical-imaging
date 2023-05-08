import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from prepareImage import *
from skimage import transform


# Function to get us some example images and their masks, and resize them 

im1= prepareImage('data/images/imgs_part_1/PAT_9_17_80.png')
mask1 = refineImage(im1, 'data/images/imgs_part_1/PAT_9_17_80.png')

plt.imshow(mask1, cmap='gray')

plt.imshow(mask1, cmap='gray')

#Total size of the image
total = mask1.shape[0] * mask1.shape[1] 

#Size of mask only
area = np.sum(mask1)

#As percentage
print(area/total*100)

# Measure DIAMETER of the lesion: measure height or width of the mask

#How many 1's in each column of the image (sum over axis 0, i.e. rows)
pixels_in_col = np.sum(mask1, axis=0)
print(mask1.shape)
print(pixels_in_col.shape)


#Without this there are some non zeros and ones still because of the resizing
pixels2 = pixels_in_col > 0
pixels2 = pixels2.astype(np.int8)

print(pixels2)

#pixels in a row 
max_pixels_in_col = np.max(pixels_in_col)
print('height is', max_pixels_in_col)

# Measuring the diameter at an angle

# General rule of thumb - create a simpler image first, then do the measurement

#rot_im = transform.rotate(mask1, 45)
#plt.imshow(rot_im, cmap='gray')

# Now we can measure as before by counting pixels in rows/columns...