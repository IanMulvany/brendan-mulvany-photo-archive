# crop images using PIL
# see discussion here: https://stackoverflow.com/questions/9983263/how-to-crop-an-image-using-pil
# good overview of argparse - https://realpython.com/command-line-interfaces-python-argparse/

from PIL import ImageOps
from PIL import Image
import argparse
import sys
from os import path
import glob
from pathlib import Path

parser = argparse.ArgumentParser(description="Crops image")
parser.add_argument("dir_path", type=str, help="path to the image directory")

# parse arguments
args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
dir_path = args.dir_path
print("image you are cropping is: " + dir_path)

# get all images in a directory
images = glob.glob(dir_path + "/*.jpg")
print(images)

# create path to crop for images
crop_path = dir_path + "/cropped"
Path(crop_path).mkdir(parents=True, exist_ok=True)


def crop_image(image_path, crop_dimensions):
    img = Image.open(image_path)
    border = crop_dimensions  # (300, 1000, 300, 1000)  # left, top, right, bottom
    inew = ImageOps.crop(img, border)
    return inew


# crop images and save to directory.
crop_dimensions = (300, 1000, 300, 1000)
for image in images:
    cropped_image = crop_image(image, crop_dimensions)
    crop_image_path = crop_path + image.split("/")[-1]
    cropped_image.save(crop_image_path)
