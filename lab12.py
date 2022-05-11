"""
Abigail Roberts
Lab 12
"""

import sqlite3
def __init__(self):
    con = sqlite3.connect(":memory.gradebook:")
    cur = con.cursor()
    cur.execute("create table lang (student, first_appeared)")

    cur.execute("insert into lang values (?,?)", ("Greg", 46))

    lang_list = [
        ('Samantha', 97),
        ('Tommy', 84),
        ('Tonya', 76),
        ('George', 90),
        ('Everly', 62)
        ]
    cur.executemany("insert into gradebook values (?, ?)", lang_list)

    cur.execute("select * from lang where firdt_appeared=:grade", {"grade":46})
    print(cur.fetchall())

    con.close()
