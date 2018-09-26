#!/usr/bin/env python3

import sqlite3
import contextlib

db_path = "/Users/csbailleul/Documents/Test_Automation/pyspark/dataffirm_db.db"


@contextlib.contextmanager
def open_database(database):
    database_instance = sqlite3.connect(database)
    database_instance.text_factory = sqlite3.OptimizedUnicode
    yield database_instance
    database_instance.close()

@contextlib.contextmanager
def open_file(file):
    file_instance = open(file, "w")
    yield file_instance
    file_instance.close()


def main():
    with open_database(db_path) as db:
        cur = db.cursor()
        query = cur.execute("""
        select userid, track_name, count(*) from musictable group by userid, track_name;
                            """).fetchall()
    with open_file("user_track_count.txt") as f:
        for idx, row in enumerate(query):
            f.write("{}\n".format(row))

if __name__ == "__main__":
    main()
