# made some modificaions to our SQLite DB
import sqlite3

# add a new column to our database, given a column name and type
def add_new_column(path_to_db, col_name, col_type):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    cur.execute("ALTER TABLE Images ADD COLUMN " + col_name + " " + col_type)
    conn.commit()
    conn.close()
    return True


# drop a column from our database, given a column name
def drop_colum(path_to_db, col_name):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    cur.execute("ALTER TABLE Images DROP COLUMN " + col_name)
    conn.commit()
    conn.close()
    return True


# modify the type of a column, given the column name and new type
def modify_colum_type(path_to_db, col_name, col_type):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    cur.execute("ALTER TABLE Images MODIFY COLUMN " + col_name + " " + col_type)
    conn.commit()
    conn.close()
    return True
