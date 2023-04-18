from PIL import Image

def is_asymmetric(image):
    image = image.convert('L')
    flipped_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    return image.tobytes() != flipped_image.tobytes()

# Replace 'image.png' with the path to your PNG image file
image = Image.open('data/images/guide_images/PAT_8_15_820.png')
if is_asymmetric(image):
    print('The image is asymmetric')
else:
    print('The image is symmetric')
