# check what is in an SQLIte database
import sqlite3

# given a path to a database, list the columns, and column type names
def list_columns(path_to_database):
    conn = sqlite3.connect(path_to_database)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(Images)")
    columns = cur.fetchall()
    conn.close()
    return columns


# given a column name and type, check if that column name and type is in the database
def check_if_exists(column_name, type):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(Images)")
    columns = cur.fetchall()
    conn.close()
    for col in columns:
        if col[1] == column_name and col[2] == type:
            return True
    return False


db_path = "bm_image_archive.db"
cols = list_columns(db_path)
print(cols)
