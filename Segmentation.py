from prepareImage import *

# Prepare an image
filename = 'data/images/imgs_part_1/PAT_585_1130_552.png'

im2 = prepareImage(filename)
#plt.imshow(prepareImage(filename), cmap="gray")
plt.imshow(refineImage(im2), cmap="gray")
plt.show()


# Show the resulting mask next to the original image
#fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
#axes[0].imshow(im2, cmap='gray')
#axes[1].imshow(mask, cmap='gray')
#axes[0].set_title('Original Image')
# axes[1].set_title('Mask')
# fig.tight_layout()
# plt.show()
