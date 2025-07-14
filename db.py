import sqlite3

# db has tables:
# 1. segments
# 2. courses
# 3. holidays
# 4. attendance
# 5. theme

# format of segments is:
# | segment (int) | start (date) | end (date) |

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

def close_connection():
    con.close()
    print("!!! Connection to db closed !!!")

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

def create_holidays_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'holidays'""")
    if (res.fetchone() is None):
        print("creating holidays table")
        cur.execute("""CREATE TABLE IF NOT EXISTS holidays (
                    name varchar(50) PRIMARY KEY,
                    start DATE,
                    end DATE,
                    no_of_days INT
                    )""")

def create_attendance_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'attendance'""")
    if (res.fetchone() is None):
        print("creating attendance table")
        cur.execute("""CREATE TABLE IF NOT EXISTS attendance (
                    c_title VARCHAR(50) PRIMARY KEY,
                    s_start CHAR(1),
                    s_end CHAR(1),
                    slot VARCHAR(3),
                    no_days INT,
                    req_att_per FLOAT
                    )""")
        res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                        name = 'courses' """)
        if (res.fetchone() is not None):
            print('inserting from courses')
            cur.execute("""INSERT INTO attendance (c_title, s_start, s_end, slot)
                        SELECT c_title, s_start, s_end, slot FROM courses""")
    
def create_theme_table():
    res = cur.execute(""" SELECT name FROM sqlite_master WHERE type = 'table' AND 
                      name = 'theme'""")
    if (res.fetchone() is None):
        print("creating theme table")
        cur.execute("""CREATE TABLE IF NOT EXISTS theme (
                    theme_name VARCHAR(50)
                    )""")

# deprecated
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
        cur.execute("""INSERT INTO attendance (c_title, s_start, s_end, slot)""", (key, value[3], value[4], value[6]))
    print("inserted course successfully")
    print(get_all_courses_info())

def get_course_titles():
    return cur.execute("""SELECT c_title from courses""").fetchall()

def get_course_info(course_title):
    return cur.execute("""SELECT * FROM courses WHERE c_title=?""", (course_title,)).fetchall()

def get_course_info_from_slot(slot_text : str, slot : str):
    return cur.execute("""SELECT * FROM courses WHERE slot_text=? AND slot=?""", (slot_text, slot)).fetchall()

def get_all_courses_info():
    return cur.execute("""SELECT * FROM courses""").fetchall()

def get_courses_info_for_cal():
    return cur.execute("""SELECT slot_text, slot, c_venue, s_start, s_end FROM courses""").fetchall()

def get_timetable_courses(segment):
    res = cur.execute("""SELECT slot_text, c_venue, slot FROM courses
                      WHERE s_start <= ? AND ? <= s_end""", (segment, segment,))
    data = res.fetchall()
    if data is None or len(data) == 0:
        print(f'*** segment received is {segment}***')
        # raise LookupError("No course found. How? Given date may be beyond 6th segment")
    return data

def commit_holiday(name : str, dates : list[str] | str, n_days : int = 1):
    if type(dates) == type([]):
        cur.execute("""UPDATE holidays SET
                    name = ?, start = ?, end = ?, no_of_days = ? WHERE name = ?""", (name, dates[0], dates[1], n_days, name))
        if cur.rowcount == 0:
            cur.execute("""INSERT INTO holidays VALUES(?, ?, ?, ?)""", (name, dates[0], dates[1], n_days))
    else:
        cur.execute("""UPDATE holidays SET
                name = ?, start = ?, no_of_days = ? WHERE name = ?""", (name, dates, n_days, name))
        if cur.rowcount == 0:
            cur.execute("""INSERT INTO holidays
                        (name, start, no_of_days)
                        VALUES(?, ?, ?)""", (name, dates, n_days))
        
    print(get_all_holidays_info())

def commit_no_days(slot : str, no_days : int):
    cur.execute("""UPDATE attendance SET no_days = ? WHERE slot = ?""", (no_days, slot))
    # print(get_att_info_from_slot(slot))

def commit_req_att_per(slot : str, p : float):
    cur.execute("""UPDATE attendance SET req_att_per = ? WHERE slot = ?""", (p, slot))
    # print(get_att_info_from_slot(slot))

def get_holiday_info_from_name(name : str):
    return cur.execute("""SELECT * FROM holidays WHERE name = ?""", (name,)).fetchall()

def get_holiday_info_from_start(s : str):
    return cur.execute("""SELECT * FROM holidays WHERE start = ?""", (s,)).fetchall()

def get_all_holidays_info():
    return cur.execute("""SELECT * FROM holidays""").fetchall()

def get_all_att_info():
    return cur.execute("""SELECT * FROM attendance""").fetchall()

def get_att_info_from_slot(slot : str):
    return cur.execute("""SELECT * FROM attendance WHERE slot = ?""", (slot,)).fetchall()

def get_no_days_from_slot(slot : str):
    return cur.execute("""SELECT no_days FROM attendance WHERE slot = ?""", (slot,)).fetchall()

def get_req_att_from_slot(slot : str):
    return cur.execute("""SELECT req_att_per FROM attendance WHERE slot = ?""", (slot,)).fetchall()

def get_theme():
    return cur.execute("""SELECT * FROM theme""").fetchall()

def commit_theme(t : str):
    if get_theme() == []:
        cur.execute("""INSERT INTO theme VALUES (?)""", (t,))
        return
    cur.execute("""UPDATE theme SET theme_name = ?""", (t,))
    print("Theme:",get_theme())

def delete_course(t: tuple):
    print("******* db.delete_course CALLED**")
    x = [i.get() for i in t]
    c_title = x[0]
    cur.execute("""DELETE FROM courses WHERE c_title = ?""", (c_title,))
    cur.execute("""DELETE FROM attendance WHERE c_title = ?""", (c_title,))

def delete_holiday(t):
    print("******* db.delete_holiday CALLED**")
    name = t[0].get()
    cur.execute("""DELETE FROM holidays WHERE name = ?""", (name,))

def delete_all_tables():
    cur.execute("""DROP TABLE segments""")
    cur.execute("""DROP TABLE courses""")
    cur.execute("""DROP TABLE holidays""")
    cur.execute("""DROP TABLE attendance""")
    close_connection()