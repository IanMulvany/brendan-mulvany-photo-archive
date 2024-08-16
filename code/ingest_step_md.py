#!/usr/bin/env python3
"""
This script processes a directory of images, extracts metadata, and inserts the data into an SQLite database.
It handles one directory per scanning event, with each scan representing a batch of images from the Brendan Mulvany archive.
"""

import configparser
import argparse
import sys
import os
import glob
import sqlite3
from datetime import datetime

from get_batch_yaml import get_batch_yaml
from get_image_md import get_image_md
from quick_hash import get_perceptual_hash

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def get_image_paths(image_dir_path, process_step, image_file_extensions):
    step_dict = {"scan": "cap", "crop": "crop", "invert": "inv", "edit": "edit"}
    step_string = step_dict[process_step]
    image_paths = []
    for ext in image_file_extensions:
        search_pattern = f"*_{step_string}{ext}"
        image_paths.extend(glob.glob(os.path.join(image_dir_path, search_pattern)))
    return image_paths

def insert_batch_record(conn, batch_info):
    cur = conn.cursor()
    sqlite_insert_query = """INSERT INTO batch_info 
        (year, name, batch_number)
        VALUES (?, ?, ?)"""
    cur.execute(sqlite_insert_query, batch_info)
    conn.commit()

def insert_step_record(conn, step_info):
    cur = conn.cursor()
    sqlite_insert_query = """INSERT INTO archival_steps 
        (name, step, abs_path, pash, batch_id, image, ingest_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cur.execute(sqlite_insert_query, step_info)
    conn.commit()

def main():
    parser = argparse.ArgumentParser(
        description="Process images and insert metadata into SQLite database",
        epilog="Happy archiving!"
    )
    parser.add_argument("image_dir_path", type=str, help="Path to the directory of scanned images")
    parser.add_argument("-s", "--step", required=True, choices=['scan', 'crop', 'invert', 'edit'], help="Image processing step")
    parser.add_argument("--config", default="config.ini", help="Path to the configuration file")
    args = parser.parse_args()

    if not os.path.isdir(args.image_dir_path):
        print(f"Error: No such directory exists: {args.image_dir_path}")
        sys.exit(1)

    config = load_config(args.config)
    db_path = config["sqlite3"]["db_path"]
    image_file_extensions = [f".{ext.strip()}" for ext in config["image_related"]["image_file_extensions"].split(",")]

    image_paths = get_image_paths(args.image_dir_path, args.step, image_file_extensions)
    if not image_paths:
        print(f"No images found in {args.image_dir_path} for step {args.step}")
        sys.exit(1)

    batch_year, batch_number, batch_note = get_batch_yaml(args.image_dir_path)
    
    try:
        conn = sqlite3.connect(db_path)
        insert_batch_record(conn, [batch_year, batch_note, batch_number])

        for image_path in image_paths:
            image_name, image_date, image_absolute_path = get_image_md(image_path)
            pash = get_perceptual_hash(image_path)
            step_info = [image_name, args.step, image_absolute_path, str(pash), batch_number, image_name, datetime.now().isoformat()]
            insert_step_record(conn, step_info)

        conn.close()
        print(f"Successfully processed {len(image_paths)} images and inserted metadata into the database.")
    except sqlite3.Error as error:
        print(f"An error occurred while working with the SQLite database: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
