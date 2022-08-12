#!/Users/devian/opt/anaconda3/envs/bm_archive/bin/python
import yaml
import sys 
import argparse
from os import path 
from get_batch_info import get_batch_number
from get_batch_info import get_batch_year
from get_batch_info import get_batch_note

# write a YAML file that embeds the following information 
# - batch year: a number 
# - batch number: a number
# - batch note: a string 

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

def write_batch_yaml(path, batch_year, batch_number, batch_note):
    batch_info = {
        "batch_year": batch_year,
        "batch_number": batch_number,
        "batch_note": batch_note
    }
    with open(path+ "/" + "batch_info.yaml", "w") as f:
        yaml.dump(batch_info, f)


batch_year = get_batch_year()
batch_number = get_batch_number()
batch_note = get_batch_note() 

write_batch_yaml(image_dir_path, batch_year, batch_number, batch_note)

