
from colourfeaturetest import *
from symmetrytest import *
from diameter import *
from imagesegmentation import *

def main():
    # loop through each image in the folder and apply the appropiate methods and write to the csv file
    # for each image in folder
        # segmented_image = segment the image method
        # symmetry = symmetrymethod(segmented_image)
        # color_variance = colormethod(segmented_image)
        # diameter = diametermethod(segmented_image)

        # write the results to .csv file, maybe make a method for that?
    segmented_image = segmentImage("data/images/guide_images/PAT_72_110_647.png")
    symmetry = getSymmetry("data/images/guide_images/PAT_72_110_647.png")
    Rvar, gvar, bvar = exact_color("data/images/guide_images/PAT_72_110_647.png", 900, 12, 2.5)
    diameter = getDiameter("data/images/guide_images/PAT_72_110_647.png")
    print("Symmetry classifier of lesion: " + str(symmetry))
    print("RGB Variance: R: " + str(Rvar) + " G: "+ str(gvar) + " B: "+str(bvar))
    print("Diameter of lesion: " + str(diameter))

    # folder_dir = "data/images/guide_images"
    # for images in os.listdir(folder_dir):
    #     # check if the image ends with png
    #     if (images.endswith(".png")):
    #         print(is_symmetric(f"{folder_dir}/{images}"))


if __name__ == "__main__":
    main()
