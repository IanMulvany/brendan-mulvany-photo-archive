#!/Users/devian/opt/anaconda3/envs/bm_archive/bin/python
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
import sqlite3 

#
from get_batch_info import get_batch_info
from get_image_md import get_image_md
from quick_hash import get_image_hashes

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
#TODO: configure db filed names from ini file rather than in code
images_md = []
for image_path in image_paths:
    image_date, image_name, image_size, image_absolute_path = get_image_md(image_path)
    image_hash, near_hash = get_image_hashes(image_path)
    # set row to the order of items in the insert query below
    row = [image_date, image_absolute_path, image_name, image_size, image_hash, str(near_hash)]
    images_md.append(row)

# get info about the batch run.
batch_number, batch_year, batch_note = get_batch_info()

for row in images_md:
    row.extend([batch_year, batch_number, batch_note]) # add batch info to row 


# insert the following data into the Images table of the Sqlite database
# capture_date
# impage_path
# image_name 
# image_size
# md5_hash 
# near_hash (pash) 
# batch_year 
# batch_number 
# batch_note 

print(db_path)
def insertMultipleRecords(db_path, recordList):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Images 
            (capture_date, image_path, image_name, image_size, image_hash, near_hash, bm_batch_year, bm_batch_number, bm_batch_note) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            
        # cur.execute("INSERT INTO Images VALUES (9, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
        cur.executemany(sqlite_insert_query, recordList) 
        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to insert record into sqlite table", error)


insertMultipleRecords(db_path, images_md)
print("done") 