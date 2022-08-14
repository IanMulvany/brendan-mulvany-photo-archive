#!/Users/devian/opt/anaconda3/envs/bm_archive/bin/python
"""
Rename the captured image files based on the process setp

"""
import configparser
import argparse
import sys
from os import path
import glob as glob
from os.path import join
import exifread

config = configparser.ConfigParser()
config.read("config.ini")
extensions_string = config["image_related"]["image_file_extensions"]
extensions_string_stripped = extensions_string.lstrip('"').rstrip('"')
image_file_extensions = ["." + x for x in extensions_string_stripped.split(",")]

# use argparse to get the path to the image files
parser = argparse.ArgumentParser(
    prog="scanned_images_md_to_sqlite",
    description="Get some metadata about the images in a directory",
    epilog="good scanning!!",
)
parser.add_argument(
    "image_dir_path", type=str, help="path to the directory of scanned images"
)

def get_image_paths(image_dir_path):
    image_paths = [] 
    for ext in image_file_extensions:
        search_pattern = "*" + ext 
        print(search_pattern)
        image_paths.extend(glob.glob(join(image_dir_path, search_pattern)))
    return image_paths



args = parser.parse_args()
image_dir_path = args.image_dir_path

if path.isdir(image_dir_path) is False:
    print("error, no such directory exists: " + image_dir_path)
    sys.exit()

image_paths = get_image_paths(image_dir_path)  
print("files to renname are: ")
print(image_paths)

def get_created_date_from_exif(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
        created_date = tags["EXIF DateTimeOriginal"].values
    return created_date

for image_path in image_paths:
    l_ip = image_path.split("/")[-1].lower() 
    l_ip_nws = l_ip.replace(" ", "_") 
    print(l_ip_nws) 
    created_date = get_created_date_from_exif(image_path) 
    print(created_date)

    