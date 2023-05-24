
from colourfeaturetest import *
from symmetrytest import *
from diameter import *
from imagesegmentation import *
import csv
import os


def main():
    # loop through each image in the folder and apply the appropiate methods and write to the csv file
    # for each image in folder
    # image_id = os.path.basename(os.path.normpath(
    #     'data/images/guide_images/PAT_72_110_647.png'))
    # symmetry = getSymmetry("data/images/guide_images/PAT_72_110_647.png")
    # Rvar, gvar, bvar = exact_color(
    #     "data/images/guide_images/PAT_72_110_647.png", 900, 12, 2.5)
    # diameter = getDiameter("data/images/guide_images/PAT_72_110_647.png")

    # headers = ["image_id", "asymmetry", "R_color_variance",
    #            "G_color_variance", "B_color_variance", "diameter", "healthy"]
    # data = [image_id, symmetry, Rvar, gvar, bvar, diameter, "1"]

    added = 0
    addedcancer = 0
    folder_dir = "data/images/imgs_part_1"
    headers = ["image_id", "asymmetry", "R_color_variance",
               "G_color_variance", "B_color_variance", "diameter", "diagnosis", "healthy"]
    with open('featuresFile.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        filename = 'data/metadata.csv'
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                # because of bad segmentation
                if (row[-9] == "SCC" or row[-9] == "MEL") and addedcancer < 70:
                    for image in os.listdir(folder_dir):
                        if row[-2] == image:
                            image_id = image
                            symmetry = getSymmetry(
                                f"data/images/imgs_part_1/{image}")
                            Rvar, gvar, bvar = exact_color(
                                f"data/images/imgs_part_1/{image}", 900, 12, 2.5)
                            healthy = 1
                            diameter = getDiameter(
                                f"data/images/imgs_part_1/{image}")
                            if row[-9] == "MEL" or row[-9] == "SCC":
                                healthy = 0
                            data = [image_id, symmetry, Rvar,
                                    gvar, bvar, diameter, row[-9], healthy]
                            writer.writerow(data)
                            added += 1
                            addedcancer += 1
                            # print(added)
                            if added == 204:
                                return
                if row[-9] == "NEV" or row[-9] == "SEK":
                    for image in os.listdir(folder_dir):
                        if row[-2] == image:
                            image_id = image
                            symmetry = getSymmetry(
                                f"data/images/imgs_part_1/{image}")
                            Rvar, gvar, bvar = exact_color(
                                f"data/images/imgs_part_1/{image}", 900, 12, 2.5)
                            healthy = 1
                            diameter = getDiameter(
                                f"data/images/imgs_part_1/{image}")
                            if row[-9] == "MEL" or row[-9] == "SCC":
                                healthy = 0
                            data = [image_id, symmetry, Rvar,
                                    gvar, bvar, diameter, row[-9], healthy]
                            writer.writerow(data)
                            added += 1
                            # print(added)
                            if added == 204:
                                return
                            # print('except')
                            # continue
                        # print(image)
    # folder_dir = "data/images/guide_images"
    # for images in os.listdir(folder_dir):
    #     # check if the image ends with png
    #     if (images.endswith(".png")):
    #         print(is_symmetric(f"{folder_dir}/{images}"))


if __name__ == "__main__":
    main()
