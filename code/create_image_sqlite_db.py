# This file creates an SQLite database for storing info about image

import sqlite3

# Create an SQLite database for storing info about images that contains the following columns:
# - image_id: unique identifier for each image
# - capture_date: timestamp
# - image_path: path to the image
# - image_name: name of the image
# - image_size: size of the image in bytes
# - image_hash: hash of the image


def create_image_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Images")
    cur.execute(
        "CREATE TABLE Images (image_id INTEGER PRIMARY KEY, capture_date TEXT, image_path TEXT, image_name TEXT, image_size INTEGER, image_hash TEXT)"
    )
    conn.commit()
    conn.close()


db_path = "bm_image_archive.db"
create_image_db(db_path)
