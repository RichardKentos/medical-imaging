import statistics
import extcolors
from imagesegmentation import *

from PIL import Image

"""
Extract the exact colors and calculate color variances from an input image.

This function resizes the input image, extracts the colors using a given tolerance, and calculates the variances of
the red, green, and blue color channels. If there are multiple colors extracted, the variances are returned. If
there is only one color or no colors extracted, zero variances are returned.

Args:
    input_image (numpy.ndarray): The input image as a NumPy array.
    resize (int): The desired width of the image after resizing.
    tolerance (int): The tolerance value for color extraction.
    zoom (float): The zoom factor for resizing the image.

Returns:
    tuple: A tuple containing the red, green, and blue color variances. If there are multiple colors extracted,
        the variances are returned. Otherwise, zero variances are returned.
"""


def exact_color(input_image, resize, tolerance, zoom):

    # resize
    output_width = resize
    img = Image.fromarray((input_image * 255).astype(np.uint8))
    if img.size[0] >= resize:
        wpercent = (output_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((output_width, hsize), Image.ANTIALIAS)

    colors_x = extcolors.extract_from_image(img, tolerance=tolerance, limit=13)

    colors_pre_list = str(colors_x).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]

    r_list = []
    g_list = []
    b_list = []

    for i in df_rgb:  # does it for how many colours there are, so this one 3 times
        r_list.append(int(i.split(", ")[0].replace("(", "")))
        g_list.append(int(i.split(", ")[1]), )
        b_list.append(int(i.split(", ")[2].replace(")", "")))
    if len(r_list) > 1 or len(g_list) > 1 or len(b_list) > 1:
        r_var = statistics.variance(r_list)
        g_var = statistics.variance(g_list)
        b_var = statistics.variance(b_list)
        return r_var, g_var, b_var
    else:
        return 0, 0, 0