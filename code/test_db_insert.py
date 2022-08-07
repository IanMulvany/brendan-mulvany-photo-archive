import sqlite3

from click import CommandCollection
 
 # insert some dummy data into the db bm_image_archive.db 
def insert_dummy_data(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO Images VALUES (1, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (2, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (3, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (4, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (5, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (6, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO Images VALUES (7, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")

    cur.execute("INSERT INTO FieldDescription VALUES (1, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO FieldDescription VALUES (2, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO FieldDescription VALUES (3, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")
    cur.execute("INSERT INTO FieldDescription VALUES (4, '2019-01-01', 'image_path', 'image_name', 100, 'image_hash', 'near_hash', 'bm_batch_year', 1, 'bm_batch_note')")

    conn.commit()
    conn.close()

db_path = "bm_image_archive.db"
insert_dummy_data(db_path)
