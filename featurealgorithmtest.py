from PIL import Image

def is_asymmetric(image):
    image = image.convert('L')
    flipped_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    image_data = list(image.getdata())
    flipped_data = list(flipped_image.getdata())
    return image_data != flipped_data

# Replace 'image.png' with the path to your PNG image file
image = Image.open('data/images/guide_images/PAT_89_135_11.png')
if is_asymmetric(image):
    print('The image is asymmetric')
else:
    print('The image is symmetric')
