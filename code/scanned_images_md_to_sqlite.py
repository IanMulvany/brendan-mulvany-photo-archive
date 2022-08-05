"""
Given a path to a directory of images:

- get core metadata about these images, and insert that data into Mysqllite database. 

We assume that there is one directory per scanning event, and each scan is for one 
batch of images from the Brendan Mulvany archive. 
"""

import configparser
import argparse
import sys
from os import path
import glob as glob
from os.path import join

#
from get_batch_info import get_batch_info
from get_image_md import get_image_md

# Get some config data about the location of the myslite db
config = configparser.ConfigParser()
config.read("config.ini")
db_path = config["sqlite3"]["db_path"]
extensions_string = config["image_related"]["image_file_extensions"]
extensions_string_stripped = extensions_string.lstrip('"').rstrip('"')
image_file_extensions = ["*." + x for x in extensions_string_stripped.split(",")]
print(image_file_extensions)


# use argparse to get the path to the image files
parser = argparse.ArgumentParser(
    prog="scanned_images_md_to_sqlite",
    description="Get some metadata about the images in a directory",
    epilog="good scanning!!",
)
parser.add_argument(
    "image_dir_path", type=str, help="path to the directory of scanned images"
)
args = parser.parse_args()
image_dir_path = args.image_dir_path
if path.isdir(image_dir_path) is False:
    print("error, no such directory exists: " + image_dir_path)
    sys.exit()


# get path to image files in the image_dir_path directory
def get_image_paths(image_dir_path):
    image_paths = []
    for ext in image_file_extensions:
        image_paths.extend(glob.glob(join(image_dir_path, ext)))
    return image_paths


image_paths = get_image_paths(image_dir_path)

# get the md for each image in image paths
for image_path in image_paths:
    image_date, image_name, image_size, image_absolute_path = get_image_md(image_path)
    print(image_date, image_name, image_size, image_absolute_path)


# get info about the batch run.
batch_number, batch_year, batch_note = get_batch_info()
print(batch_number, batch_year, batch_note)
