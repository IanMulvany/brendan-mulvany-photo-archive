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

#
from get_batch_info import get_batch_info

# Get some config data about the location of the myslite db
config = configparser.ConfigParser()
config.read("config.ini")
db_path = config["sqlite3"]["db_path"]
print(db_path)


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

# get info about the batch run.
batch_number, batch_year, batch_note = get_batch_info()
print(batch_number, batch_year, batch_note)
