#!/opt/homebrew/bin/python3
"""
This script has some functions for getting metadata about images. 
We want to know

- the capture date - extracted from the Exif data 
- file size 
- file name 
- the absolute path of the image 

To test the function quickly run as:

$ ./get_image_md.py  
"""


import exifread
from datetime import datetime
from os import path
from PIL import Image
import sys
import os

# given a path to an impge, extract the exif date from the image file
def get_image_date(image_path):

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    with open(image_path, "rb") as f:
        tags = exifread.process_file(f)
        date = tags.get("EXIF DateTimeOriginal")
        if date is not None:
            date = datetime.strptime(str(date), "%Y:%m:%d %H:%M:%S")
            return date
        else:
            return None


# given a path to an impge, get the image name
def get_image_name(image_path):

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    return image_path.split("/")[-1]


# given a path to an impge, get the file size
def get_image_size(image_path):

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    file_stats = os.stat(image_path)
    file_size = file_stats.st_size
    return file_size


# given the relative path of an image, return the absolute path
def get_absolute_path(image_path):

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    return os.path.abspath(image_path)


def get_image_md(image_path):
    "get some metadata about the image"

    if path.isfile(image_path) is False:
        print("error, no such file exists")
        sys.exit()

    image_date = get_image_date(image_path)
    image_name = get_image_name(image_path)
    image_size = get_image_size(image_path)
    image_absolute_path = get_absolute_path(image_path)

    return image_date, image_name, image_size, image_absolute_path


# create the main function to run the program
def main():
    "main function"

    test_image_path = "../images/test_images/JPEG image 6.jpeg"
    image_date = get_image_date(test_image_path)
    image_name = get_image_name(test_image_path)
    image_size = get_image_size(test_image_path)
    image_absolute_path = get_absolute_path(test_image_path)

    print(image_date)
    print(image_name)
    print(image_size)
    print(image_absolute_path)


if __name__ == "__main__":
    main()
    sys.exit()
