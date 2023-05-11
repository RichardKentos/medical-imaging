
from skimage.segmentation import slic, mark_boundaries
from prepareImage import *
from matplotlib import *
from main import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

im1= segmentImage('data/images/imgs_part_1/PAT_9_17_80.png')
example_im = im1

# Divide the pixels into segments of similar color
segments_slic = slic(example_im, n_segments=10, compactness=3, sigma=3, start_label=1, channel_axis=None)


# Show the results
fig, ax = plt.subplots(1, 2, figsize=(10, 10), sharex=True, sharey=True)

ax[0].imshow(example_im)
ax[0].set_title("Original")

ax[1].imshow(mark_boundaries(example_im, segments_slic))
ax[1].set_title('SLIC')

plt.tight_layout()
plt.show()

# What kind of features can you now measure, combining this with the mask?