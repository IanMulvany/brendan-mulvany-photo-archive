"""
Given a path to a directory of images:

- get core metadata about these images, and insert that data into Mysqllite database. 

We assume that there is one directory per scanning event, and each scan is for one 
batch of images from the Brendan Mulvany archive. 
"""

import configparser
import argparse

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
print("images you are looking at are in the directory: " + image_dir_path)
