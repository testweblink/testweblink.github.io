from PIL import Image
import PIL
import os
import glob

def convert_image(image_path, image_type):

    # 1. Opening the image:
    im = Image.open(image_path)
    # 2. Converting the image to RGB colour:
    im = im.convert('RGB')
    # 3. Spliting the image path (to avoid the .jpg or .webp being part of the image name):
    image_name = image_path.split('.')[0]
    print(f"This is the image name: {image_name}")

    # Saving the images based upon their specific type:
    if image_type == 'jpg' or image_type == 'PNG':
        im.save(f"{image_name}.webp", 'webp')
    else:
        # Raising an error if we didn't get a jpeg or webp file type!
        raise Error

files = os.listdir() # We list all of the files and folders using os.listdir()

images = [file for file in files if file.endswith(('jpg', 'PNG'))]

for image in images:
    if image.endswith('jpg'):
        convert_image(image, image_type='jpg')
    elif image.endswith('PNG'):
        convert_image(image, image_type='PNG')
    else:
        raise Error
