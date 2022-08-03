"""
Given a path to a directory of images:

- get core metadata about these images, and insert that data into Mysqllite database. 

We assume that there is one directory per scanning event, and each scan is for one 
batch of images from the Brendan Mulvany archive. 
"""

# Get some config data about the location of the myslite db
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
db_path = config["sqlite3"]["db_path"]

print(db_path)
