# Image Archiving Application

This repository contains a collection of Python scripts designed for an image archiving application. The scripts handle various aspects of image processing, metadata extraction, and database management.

## Key Components

1. **Database Interaction (check_db_status.py)**
   - Provides functions to interact with a SQLite database.
   - Lists tables in the database.
   - Shows columns in the 'Images' table.
   - Counts records in the 'Images' table.
   - Checks if specific columns exist in the table.

   Example usage:
   ```
   python check_db_status.py --db path/to/your/database.db
   ```
   If no --db argument is provided, the script will use 'bm_image_archive.db' in the current directory.

2. **Contact Sheet Creation (contact_sheet.py)**
   - Creates a contact sheet (montage) of images from a specified directory.
   - Arranges image thumbnails into a customizable grid layout.
   - Allows specification of columns, rows, thumbnail size, margins, and padding.
   - Automatically generates an output filename based on the directory name and current date/time.
   - Saves the contact sheet as a PNG file in the same directory as the input images.

   Example usage:
   ```
   python contact_sheet.py /path/to/image/directory --cols 5 --rows 4
   ```
   This will create a contact sheet with 5 columns and 4 rows using images from the specified directory.

3. **Database Creation (create_image_sqlite_db.py)**
   - Creates a SQLite database for storing image information.
   - Sets up tables for image metadata and field descriptions.

4. **Metadata Extraction**
   - Various scripts (e.g., get_image_md.py) extract metadata from images.
   - Handles information like image name, date, path, and size.

5. **Batch Information Management**
   - Scripts for retrieving and storing batch information.
   - Includes YAML file manipulation for batch data.

6. **Image Processing**
   - Scripts for image hashing (quick_hash.py).
   - Image renaming and cropping functionalities.

## Usage

Each script can be run independently. Refer to individual script headers or use the --help flag for specific usage instructions.

## Dependencies

Ensure you have the required libraries installed. You can install them using:

```
pip install -r requirements.txt
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
~/D/c/b/code $ more *.py | llm -s "describe what each of these files does" -m gpt4
The files described here all contribute to an archiving application for images, which extracts some metadata about scanned images (like image size, location, capture time, image hash, etc.) and stores them in an SQLite database for easy retrieval and manipulation. Here is a brief description of each file :

1. Image metadata extraction files: These scripts are designed to extract metadata from images and SQLite databases. They use the sqlite3 and PIL libraries to interact with SQLite databases and image files respectively. These include functions to list, add, modify and delete columns in an SQLite database table. There are also functions to extract image metadata such as name, date, path and size.

2. Image manipulation files: This script makes use of PIL to open and manipulate images. Specifically, this file contains a function that creates a contact sheet from a group of filenames.

3. Database manipulation files: These scripts are used for creating an SQLite database for storing information about images. They also include the functionality to insert metadata for each image batch into the database.

4. Batch information retrieval files: These scripts ask the user for information about the photo batch. This is done through console prompts where the user enters the details. This information is then used when updating the SQLite database.

5. YAML file manipulation scripts: The scripts allow the application to read a YAML file, specifically designed to store batch image information. These scripts can create a new YAML file or update an existing file with new batch image data.

6. Image hashing scripts: These scripts are used to get unique hash values from the images, which can be used to quickly compare the images. Both MD5 and Perceptual hashing are used to create the hashes.

7. Image renaming script: This script allows for renaming of image files based on processing steps.

8. Image cropping script : This script allows the cropping of images and saving them to a defined directory. The cropping dimensions can be defined.

These scripts make up an image archiving system by providing the functionalities to extract metadata from images, manipulate images and SQLite databases, retrieve user inputs, interact with YAML files, hashing images, and conduct image processing steps.
