#!/Users/devian/opt/anaconda3/envs/bm_archive/bin/python
import yaml
import sys 
import argparse
from os import path 
from os.path import exists 

# get the folloing information from a YAML file
# - batch year: a number 
# - batch number: a number
# - batch note: a string 


def get_batch_yaml(path):

    yaml_path = path + "/" + "batch_info.yaml"
    print(yaml_path)

    if exists(yaml_path) is False:
        print("error, no such file exists: " + yaml_path)
        sys.exit()

    with open(yaml_path, "r") as f:
        batch_info = yaml.load(f, Loader=yaml.FullLoader)
    return batch_info["batch_year"], batch_info["batch_number"], batch_info["batch_note"]


def main():
    parser = argparse.ArgumentParser(
        prog="scanned_images_md_to_sqlite",
        description="Get some metadata about the images in a directory",
        epilog="good scanning!!",)

    parser.add_argument(
        "image_dir_path", type=str, help="path to the directory of scanned images"
    )

    args = parser.parse_args()
    image_path = args.image_dir_path 
    batch_year, batch_number, batch_note = get_batch_yaml(image_path)
    print(batch_year, batch_number, batch_note)

if __name__ == "__main__":
    main()