# About 

This file contains sqlite-utils commands that we run on the database. 

refactoring based on https://simonwillison.net/2020/Sep/23/sqlite-utils-extract/ 
```bash
sqlite-utils extract bm_image_archive_test_refactor.db Images \
   'bm_batch_year' 'bm_batch_number' 'bm_batch_note' \
  --table 'bm_batch_info' \
  --fk-column 'bm_batch_number' \
  --rename 'bm_batch_year' capture_year \
  --rename 'bm_batch_number' number \
  --rename 'bm_batch_note' name 
```

based on this query example: 
```bash
sqlite-utils extract salaries.db salaries \
   'Organization Group Code' 'Organization Group' \
  --table 'organization_groups' \
  --fk-column 'organization_group_id' \
  --rename 'Organization Group Code' code \
  --rename 'Organization Group' name
```

--
insertint images into sqlite

```bash
sqlite-utils insert-files bm_image_archive_test_refactor.db original_images ../images/test_images -c path -c md5 -c last_modified:mtime -c size --pk=path 
```

```bash
(bm_archive) devian@JBHM-LT25194 code % sqlite-utils insert-files bm_image_archive_test_refactor.db original_images_blobs ../images/test_images
``` 

This should work:

sqlite-utils insert-files files.db images *.gif -c blob:content -c hashed_md5:md5

Produces this schema:

CREATE TABLE [images] (
   [blob] BLOB,
   [hashed_md5] TEXT
);

See here for more details https://sqlite-utils.datasette.io/en/stable/cli.html#cli-insert-files

Try this command:

```bash
sqlite-utils insert-files bm_image_archive_test_refactor.db images_blob_and_md ../images/osx-export-1  -c blob:content -c hashed_md5:md5 -name -c ctime_iso:created_time -c size 
```




---
userful SQL 

select
  image_id,
  capture_date,
  image_name,
  bm_batch_number,
  bm_batch_info.name,
  bm_batch_info.capture_year
from
  Images
  Join bm_batch_info on bm_batch_number 


--- --------------------------------
Creating multiple tables with keys 

from : https://stackoverflow.com/questions/62625913/inserting-with-foreign-key-in-sqlite3-for-python 

CREATE TABLE "team" (
    "id"    INTEGER UNIQUE,
    "opponent_name" TEXT,
    "rank_when played"  INTEGER,
    "date_added"    TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "game" (
    "id"    INTEGER,
    "opponent_id"   INTEGER,
    "goals_for" INTEGER,
    "goals_against" INTEGER,
    "date_added"    TEXT,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("opponent_id") REFERENCES "team"("id")
);


---
info on creating indicies in SQLite database

https://www.sqlitetutorial.net/sqlite-index/
see also https://sqlite-utils.datasette.io/en/stable/cli.html#creating-indexes 

