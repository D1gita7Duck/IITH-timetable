import sqlite3

# db has tables:
# 1. slot_text


# format of slot text is:
# slot (primary key)(varchar(3))    text (varchar(30))


def initialize_db():
    """
    Connects/creates the database if it does/doesn't exist. 
    """
    global con
    global cur
    con = sqlite3.connect(database="database.db", autocommit=True)
    cur = con.cursor()

def create_slots_text_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'slot_text' """)
    if (res.fetchone() is None):
        print("creating new table")
        cur.execute("""CREATE TABLE IF NOT EXISTS slot_text (
                    slot VARCHAR(3) PRIMARY KEY,
                    text VARCHAR(30)
                    )""")
        cur.execute("""INSERT INTO slot_text VALUES ('A', 'A')""")
        cur.execute("""INSERT INTO slot_text VALUES ('B', 'B')""")
        cur.execute("""INSERT INTO slot_text VALUES ('C', 'C')""")
        cur.execute("""INSERT INTO slot_text VALUES ('D', 'D')""")
        cur.execute("""INSERT INTO slot_text VALUES ('E', 'E')""")
        cur.execute("""INSERT INTO slot_text VALUES ('F', 'F')""")
        cur.execute("""INSERT INTO slot_text VALUES ('G', 'G')""")
        cur.execute("""INSERT INTO slot_text VALUES ('P', 'P')""")
        cur.execute("""INSERT INTO slot_text VALUES ('Q', 'Q')""")
        cur.execute("""INSERT INTO slot_text VALUES ('R', 'R')""")
        cur.execute("""INSERT INTO slot_text VALUES ('S', 'S')""")
        cur.execute("""INSERT INTO slot_text VALUES ('FN1', 'FN1')""")
        cur.execute("""INSERT INTO slot_text VALUES ('FN2', 'FN2')""")
        cur.execute("""INSERT INTO slot_text VALUES ('FN3', 'FN3')""")
        cur.execute("""INSERT INTO slot_text VALUES ('FN4', 'FN4')""")
        cur.execute("""INSERT INTO slot_text VALUES ('FN5', 'FN5')""")
        cur.execute("""INSERT INTO slot_text VALUES ('AN1', 'AN1')""")
        cur.execute("""INSERT INTO slot_text VALUES ('AN2', 'AN2')""")
        cur.execute("""INSERT INTO slot_text VALUES ('AN3', 'AN3')""")
        cur.execute("""INSERT INTO slot_text VALUES ('AN4', 'AN4')""")
        cur.execute("""INSERT INTO slot_text VALUES ('AN5', 'AN5')""")

def get_slot_text():
    result = cur.execute("""SELECT * FROM slot_text""").fetchall()
    return result


def write_button_text(slot : str, text : str):
    cur.execute("""UPDATE slot_text SET text = ? WHERE slot = ?""", (text, slot))
    print("*** slot text updated ***")