import sqlite3
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Check the status of an SQLite database.")
    parser.add_argument("--db", default="bm_image_archive.db", help="Path to the SQLite database file")
    return parser.parse_args()

def list_database_info(path_to_database):
    print(f"Analyzing database: {path_to_database}")
    conn = sqlite3.connect(path_to_database)
    cur = conn.cursor()

    # List all tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("\nTables in the database:")
    for table in tables:
        print(f"  - {table[0]}")

    # List columns in the Images table
    cur.execute("PRAGMA table_info(Images)")
    columns = cur.fetchall()
    print("\nColumns in the 'Images' table:")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")

    # Count records in the Images table
    cur.execute("SELECT COUNT(*) FROM Images")
    count = cur.fetchone()[0]
    print(f"\nNumber of records in the Images table: {count}")

    conn.close()
    return columns

def check_if_exists(column_name, type, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(Images)")
    columns = cur.fetchall()
    conn.close()
    for col in columns:
        if col[1] == column_name and col[2] == type:
            return True
    return False

def main():
    args = parse_arguments()
    db_path = args.db

    if not os.path.exists(db_path):
        print(f"Error: The database file '{db_path}' does not exist.")
        print("Usage: python check_db_status.py [--db PATH_TO_DATABASE]")
        print("If no --db argument is provided, the script will use 'bm_image_archive.db' in the current directory.")
        return

    try:
        list_database_info(db_path)
    except sqlite3.Error as e:
        print(f"An error occurred while accessing the database: {e}")

if __name__ == "__main__":
    main()
