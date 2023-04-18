from pathlib import Path
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


def prepareImage(imageName):
    filename = Path(f'data/images/imgs_part_1/{imageName}')  # PAT_8_15_820.png
    im = plt.imread(filename)
    im2 = im[0:1500, :, :3]  # Select only the first three channels (RGB)
    im2 = rgb2gray(im2)*256
    return im2
