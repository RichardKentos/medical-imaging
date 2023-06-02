from colourfeaturetest import *
from symmetrytest import *
from diameter import *
from imagesegmentation import *
import csv
import os

"""
This function processes a set of images and extracts features from them.
It writes the extracted data to a CSV file named 'featuresFile.csv'.

Parameters:
    None

Returns:
    None
"""

def main():
    # loop through each image in the folder and apply the appropiate methods and write to the csv file
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
                if (row[-9] == "SCC" or row[-9] == "MEL") and addedcancer < 95:
                    for image in os.listdir(folder_dir):
                        if row[-2] == image:
                            image_id = image
                            segmentedImage = segmentImage(f"data/images/imgs_part_1/{image}")
                            symmetry = getSymmetry(segmentedImage)
                            Rvar, gvar, bvar = exact_color(segmentedImage, 900, 12, 2.5)
                            healthy = 0
                            diameter = getDiameter(segmentedImage)
                            data = [image_id, symmetry, Rvar, gvar, bvar, diameter, row[-9], healthy]
                            writer.writerow(data)
                            added += 1
                            addedcancer += 1
                            if added == 204:
                                return
                if row[-9] == "NEV" or row[-9] == "SEK":
                    for image in os.listdir(folder_dir):
                        if row[-2] == image:
                            image_id = image
                            segmentedImage = segmentImage(f"data/images/imgs_part_1/{image}")
                            symmetry = getSymmetry(segmentedImage)
                            Rvar, gvar, bvar = exact_color(segmentedImage, 900, 12, 2.5)
                            healthy = 1
                            diameter = getDiameter(segmentedImage)
                            data = [image_id, symmetry, Rvar, gvar, bvar, diameter, row[-9], healthy]
                            writer.writerow(data)
                            added += 1
                            if added == 204:
                                return


if __name__ == "__main__":
    main()
