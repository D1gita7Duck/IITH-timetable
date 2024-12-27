import sqlite3

# db has tables:
# 1. slot_text
# 2. segments
# 3. courses


# format of slot text is:
# slot (primary key)(varchar(3))    text (varchar(30))

# format of segments is:
# | segment (int) | start_date (date) | end_date (date) |

# format of courses is:
# | course title (varchar 100)|c_code varchar 6|c_venue varchar 6|s_start char 1|s_end char 1|slot_text varchar 12|slot varchar 3|

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

def create_segments_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'segments' """)
    if (res.fetchone() is None):
        print("creating segments table")
        cur.execute("""CREATE TABLE IF NOT EXISTS segments (
                    segment VARCHAR(1) PRIMARY KEY,
                    start DATE,
                    end DATE
                    )""")
    
def create_courses_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'courses' """)
    if (res.fetchone() is None):
        print("creating courses table")
        cur.execute("""CREATE TABLE IF NOT EXISTS courses (
                    c_title VARCHAR(100) PRIMARY KEY,
                    c_code VARCHAR(6),
                    c_venue VARCHAR(6),
                    s_start CHAR(1),
                    s_end CHAR(1),
                    slot_text VARCHAR(12),
                    slot VARCHAR(3)
                    )""")

def get_slot_text():
    result = cur.execute("""SELECT * FROM slot_text""").fetchall()
    return result

def write_button_text(slot : str, text : str):
    cur.execute("""UPDATE slot_text SET text = ? WHERE slot = ?""", (text, slot))
    print("*** slot text updated ***")

def commit_segment_dates(segment, start, end):
    res = cur.execute("""UPDATE segments SET start = ?, end = ? WHERE segment = ?""", (start, end, segment))
    if cur.rowcount == 0:
        cur.execute("""INSERT INTO segments VALUES (?, ?, ?)""", (segment, start, end))
    print("inserted segment successfully")
    print(get_all_segments_info())

def get_segment_info(segment):
    return cur.execute("""SELECT * FROM segments WHERE segment = ?""", (segment,)).fetchall()

def get_all_segments_info():
    return cur.execute("""SELECT * FROM segments""").fetchall()

def commit_courses_info(key, value):
    cur.execute("""UPDATE courses SET
                c_code = ?, c_venue = ?, s_start = ?, s_end = ?, slot_text = ?, slot = ? 
                WHERE c_title = ?""", (value[1], value[2], value[3], value[4], value[5], value[6], key))
    if cur.rowcount == 0:
        cur.execute("""INSERT INTO courses VALUES (?, ?, ?, ?, ?, ?, ?)""", (key, value[1], value[2], value[3], value[4], value[5], value[6]))
    print("inserted course successfully")
    print(get_all_courses_info())

def get_course_titles():
    return cur.execute("""SELECT c_title from courses""").fetchall()

def get_course_info(course_title):
    return cur.execute("""SELECT * FROM courses WHERE c_title=?""", (course_title,)).fetchall()

def get_all_courses_info():
    return cur.execute("""SELECT * FROM courses""").fetchall()