#!/Users/devian/opt/anaconda3/bin/python
"""
a quick function to return the hash of an image

run as follows:
$./quick_hash.py <image_path>
"""

import hashlib
import argparse
import sys
from os import path

from PIL import Image
from numpy import imag
import imagehash

default_path = "../images/test_images/JPEG image 6.jpeg"
parser = argparse.ArgumentParser(description="Generate hashses of images")
parser.add_argument(
    "image_path", type=str, help="path to the image", nargs="?", default=default_path
)
parser.add_argument(
    "--image-hash", type=bool, default=False, help="generate an image hash using PIL"
)

# parse arguments
args = parser.parse_args()  # args=None if sys.argv[1:] else ["--help"])
image_path = args.image_path
image_hash = args.image_path


def get_hash_of_image(image_path):
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


def print_hash_variants(image_path):
    "prints the hash variants"

    img = Image.open(image_path)

    img_hash = imagehash.phash(img)
    average_hash = imagehash.average_hash(Image.open(image_path))
    dct_hash = imagehash.dhash(Image.open(image_path))
    classic_hash = get_hash_of_image(image_path)
    print(img_hash)
    print(average_hash)
    print(dct_hash)
    print(classic_hash)


# create the main function to run the program
def main():
    "main function"

    if args.image_path:
        print_hash_variants(image_path)
        if image_path == default_path:
            print("test path used, check function with --help")


if __name__ == "__main__":
    main()
    sys.exit()
