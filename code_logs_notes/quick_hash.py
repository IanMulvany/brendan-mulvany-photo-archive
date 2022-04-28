"""
a quick function to return the hash of an image
"""
import hashlib
import argparse
import sys
from os import path

from PIL import Image
import imagehash

parser = argparse.ArgumentParser(description="Generate hashses of images")
parser.add_argument("image_path", type=str, help="path to the image")
parser.add_argument(
    "--image-hash", type=bool, default=False, help="generate an image hash using PIL"
)


# parse arguments
args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])
image_path = args.image_path
image_hash = args.image_path


def get_hash_of_image(image_path):
    hasher = hashlib.md5()
    with open(image_path, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    img_hash = hasher.hexdigest()
    return img_hash


if path.isfile(image_path) is False:
    print("error, no such file exists")

print(image_hash)


hash = imagehash.average_hash(Image.open(image_path))
print(hash)

img_hash = get_hash_of_image(image_path)
print(img_hash)
