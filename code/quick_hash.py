#!/Users/devian/opt/anaconda3/bin/python
"""
a quick function to return the hash of an image

run as follows:
$./quick_hash.py <image_path>

run a quick test as follows: 
$./quick_hash.py 
"""
import hashlib
import argparse
import sys
from os import path
from PIL import Image
from numpy import imag
import imagehash


def get_md5_hash(image_path):
    "gets the hash of an image"

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    hasher = hashlib.md5()
    with open(image_path, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    img_hash = hasher.hexdigest()
    return img_hash


def get_perceptual_hash(image_path):
    """
    prints the hash variants

    based on https://towardsdatascience.com/detection-of-duplicate-images-using-image-hash-functions-4d9c53f04a75
    we are going to impliment phash to find visually simillar images
    """

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    img = Image.open(image_path)
    img_hash = imagehash.phash(img)
    return img_hash


# create the main function to run the program
def main():
    "main function"

    default_path = "../images/test_images/JPEG image 6.jpeg"

    if path.isfile(default_path) is False:
        print("error, no such file exists")
        sys.exit()

    md5_hash = get_md5_hash(default_path)
    print("md5 hash: " + md5_hash)
    perceptual_hash = get_perceptual_hash(default_path)
    print("perceptual hash: " + str(perceptual_hash))


if __name__ == "__main__":
    main()
    sys.exit()
