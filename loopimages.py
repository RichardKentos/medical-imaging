# import the modules
import os
from os import listdir

# get the path or directory
folder_dir = "data/images/guide_images"
for images in os.listdir(folder_dir):

    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg")
            or images.endswith(".jpeg")):
        # display
        print(images)
