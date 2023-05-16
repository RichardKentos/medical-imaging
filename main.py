
from colourfeaturetest import *
from symmetrytest import *
from diameter import *
from imagesegmentation import *
import csv
import os

def main():
    # loop through each image in the folder and apply the appropiate methods and write to the csv file
    # for each image in folder
    image_id = os.path.basename(os.path.normpath('data/images/guide_images/PAT_72_110_647.png'))
    symmetry = getSymmetry("data/images/guide_images/PAT_72_110_647.png")
    Rvar, gvar, bvar = exact_color("data/images/guide_images/PAT_72_110_647.png", 900, 12, 2.5)
    diameter = getDiameter("data/images/guide_images/PAT_72_110_647.png")

    headers = ["image_id","asymmetry","R_color_variance","G_color_variance","B_color_variance","diameter","diagnostic","healthy"]
    data = [image_id,symmetry,Rvar,gvar,bvar,diameter,"tbd","tbd"]

    with open('featuresFile.csv', 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(data)

    # folder_dir = "data/images/guide_images"
    # for images in os.listdir(folder_dir):
    #     # check if the image ends with png
    #     if (images.endswith(".png")):
    #         print(is_symmetric(f"{folder_dir}/{images}"))


if __name__ == "__main__":
    main()
