import statistics

from matplotlib.colors import rgb2hex
from skimage.segmentation import slic, mark_boundaries
from prepareImage import *
from matplotlib import *
from main import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import cv2
import extcolors
from main import *

from colormap import rgb2hex

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

img = Image.fromarray((mainfunction("data/images/guide_images/PAT_72_110_647.png") * 255).astype(np.uint8))


def image_colorfulness(image):
    # split the image into its respective RGB components
    (B, G, R) = cv2.split(image.astype("float"))
    # compute rg = R - G
    rg = np.absolute(R - G)
    # compute yb = 0.5 * (R + G) - B
    yb = np.absolute(0.5 * (R + G) - B)
    # compute the mean and standard deviation of both `rg` and `yb`
    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))
    # combine the mean and standard deviations
    stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))
    # derive the "colorfulness" metric and return it
    return stdRoot + (0.3 * meanRoot)


def exact_color(input_image, resize, tolerance, zoom):
    # background
    bg = 'bg.png'
    fig, ax = plt.subplots(figsize=(192, 108), dpi=10)
    fig.set_facecolor('white')
    plt.savefig(bg)
    plt.close(fig)

    # resize
    output_width = resize
    img = Image.fromarray((mainfunction(input_image) * 255).astype(np.uint8))
    if img.size[0] >= resize:
        wpercent = (output_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((output_width, hsize), Image.ANTIALIAS)
        resize_name = 'resize_' + input_image
        img.save(resize_name)
    else:
        resize_name = input_image

    # crate dataframeA
    img_url = resize_name
    colors_x = extcolors.extract_from_image(img, tolerance=tolerance, limit=13)
    #df_color = color_to_df(colors_x)

    # this here is the rgb values and the hex codes and percentages, we can do something with it
    # print(colors_x) #rgb values and occurence
    colors_pre_list = str(colors_x).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]

    r_list = []
    g_list = []
    b_list = []

    for i in df_rgb:  # does it for how many colours there are, so this one 3 times
        r_list.append(int(i.split(", ")[0].replace("(", "")))
        g_list.append(int(i.split(", ")[1]), )
        b_list.append(int(i.split(", ")[2].replace(")", "")))

    r_var = statistics.variance(r_list)
    g_var = statistics.variance(g_list)
    b_var = statistics.variance(b_list)
    return r_var,g_var,b_var
    # print(df_color)
    # annotate text
    # the rest of this isnt needed, its just to show the image and such
    # list_color = list(df_color['c_code'])
    # list_precent = [int(i) for i in list(df_color['occurence'])]
    # text_c = [c + ' ' + str(round(p * 100 / sum(list_precent), 1)) + '%' for c, p in zip(list_color, list_precent)]
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(160, 120), dpi=10)
    #
    # # donut plot
    # wedges, text = ax1.pie(list_precent,
    #                        labels=text_c,
    #                        labeldistance=1.05,
    #                        colors=list_color,
    #                        textprops={'fontsize': 150, 'color': 'black'})
    # plt.setp(wedges, width=0.3)
    #
    # # add image in the center of donut plot
    # extracted = mainfunction(resize_name)
    # imagebox = OffsetImage(extracted, zoom=zoom)
    # ab = AnnotationBbox(imagebox, (0, 0))
    # ax1.add_artist(ab)
    #
    # # color palette
    # x_posi, y_posi, y_posi2 = 160, -170, -170
    # for c in list_color:
    #     if list_color.index(c) <= 5:
    #         y_posi += 180
    #         rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor=c)
    #         ax2.add_patch(rect)
    #         ax2.text(x=x_posi + 400, y=y_posi + 100, s=c, fontdict={'fontsize': 190})
    #     else:
    #         y_posi2 += 180
    #         rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor=c)
    #         ax2.add_artist(rect)
    #         ax2.text(x=x_posi + 1400, y=y_posi2 + 100, s=c, fontdict={'fontsize': 190})
    #
    # fig.set_facecolor('white')
    # ax2.axis('off')
    # bg = plt.imread('bg.png')
    # plt.imshow(bg)
    # plt.tight_layout()
    # return plt.show()


# def color_to_df(input):
#     colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
#     df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
#     df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]
#
#     # convert RGB to HEX code
#     df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
#                            int(i.split(", ")[1]),
#                            int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]
#
#     df = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])
#     return df


print(exact_color("data/images/guide_images/PAT_72_110_647.png", 900, 12, 2.5))
