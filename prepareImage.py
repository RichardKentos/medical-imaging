from pathlib import Path
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


def prepareImage(path):
    filename = Path(f'data/images/imgs_part_1/{filename}')  # PAT_8_15_820.png
    file_im = Path(f'data/images/imgs_part_1/{filename}')  # PAT_8_15_820.png
    im = plt.imread(file_im)
    im2 = im[0:1500, :, :3]  # Select only the first three channels (RGB)
    im2 = rgb2gray(im2)*256
    return im2
