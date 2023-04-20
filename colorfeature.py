# SLIC clustering - see also https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_segmentations.html
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.segmentation import slic, mark_boundaries
from prepareImage import *

# Function to get us some example images and their masks, and resize them 
# def prepare_im(im_id):

#   filename = 'PAT_8_15_820.png'

#   im = plt.imread(path + 'example_image/' + im_id + '.jpg')
#   im = resize(im, (im.shape[0] // 4, im.shape[1] // 4), anti_aliasing=True)
 
#   gt = plt.imread(path + 'example_segmentation/' + im_id + '_segmentation.png')
#   gt = resize(gt, (gt.shape[0] // 4, gt.shape[1] // 4), anti_aliasing=False) #Setting it to True creates values that are not 0 or 1


#   return im, gt

filename = 'PAT_8_15_820.png'
im1 = prepareImage(filename)

example_im = im1

# Divide the pixels into segments of similar color
segments_slic = slic(example_im, n_segments=10, compactness=3, sigma=3, start_label=1)


# Show the results
fig, ax = plt.subplots(1, 2, figsize=(10, 10), sharex=True, sharey=True)

ax[0].imshow(example_im)
ax[0].set_title("Original")

ax[1].imshow(mark_boundaries(example_im, segments_slic))
ax[1].set_title('SLIC')

plt.tight_layout()
plt.show()

# What kind of features can you now measure, combining this with the mask?