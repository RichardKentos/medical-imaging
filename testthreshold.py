
import imageio as iio
import skimage.color
import skimage.filters


def measure_root_mass(filename, sigma=1.0):

    # read the original image, converting to grayscale on the fly
    image = iio.imread(uri=filename)

    # blur before thresholding
    blurred_image = skimage.filters.gaussian(image, sigma=sigma)

    # perform automatic thresholding to produce a binary image
    t = skimage.filters.threshold_otsu(blurred_image)
    binary_mask = blurred_image > t

    # determine root mass ratio
    #rootPixels = np.count_nonzero(binary_mask)
    #w = binary_mask.shape[1]
    #h = binary_mask.shape[0]
    #density = rootPixels / (w * h)

    return t*255

print(measure_root_mass(filename='data/images/imgs_part_1/PAT_30_41_815.png',sigma=1.5))