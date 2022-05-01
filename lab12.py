"""
Abigail Roberts
Lab 12
"""

import sqlite3
def __init__(self):
    con = sqlite3.connect(":memory.gradebook:")
    cur = con.cursor()
    cur.execute("""CREATE TABLE gradebook(student, grade)""")
    gradebook_studentgrades = [
        ('Samantha', 97),
        ('Tommy', 84),
        ('Tonya', 76),
        ('George', 90),
        ('Everly', 62)
        ]
    cur.executemany("insert into gradebook values (?, ?)", gradebook_student)
    con.commit()
    print('SELECT* FROM gradebook')
    con.close()
