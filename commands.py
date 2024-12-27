import customtkinter as ctk
import CTkMessagebox
import os
import db
import myentry

def int_2_str(n : int):
    """
    Returns string of given integer. 9 is returned as 09
    """
    if (n//10 == 0):
        return '0' + str(n)
    else:
        return str(n)

def show_warning(msg : str):
    warning_window = CTkMessagebox.CTkMessagebox(
                        title="Warning!",
                        message=msg,
                        icon="warning",
                        option_1="Retry",
                        sound=True,
                        cancel_button='cross',
                    )

def open_calendar_file():
    pass

def open_source_code():
    pass


def edit_courses():

    def write_values_from_db(c_title):
        print("jere", c_title)
        data = db.get_course_info(c_title)
        print(data)
        if len(data) == 0:
            print("yerror, but how?")
            return
        entry_frame.set_entries_to_given_values(c_title, data[0])

    edit_course_win = ctk.CTkToplevel(fg_color = '#121212')
    
    edit_course_win.title("Edit Course Details")
    edit_course_win.resizable(False, False)
    # set transparency to 0 until window is completely rendered
    edit_course_win.attributes("-alpha", 0)
    edit_course_win.update_idletasks()

    edit_course_win_width=700
    edit_course_win_height=600
    screen_width=2200
    screen_height=1200
    x_coordinate=int((screen_width/2)-(edit_course_win_width/2))
    y_coordinate = int((screen_height/2) - (edit_course_win_height/2))
    edit_course_win.geometry("{}x{}+{}+{}".format(edit_course_win_width, edit_course_win_height, x_coordinate, y_coordinate))

    courses = db.get_course_titles()
    if len(courses) == 0:
        courses = None
    else:
        courses = [x[0] for x in courses]

    entry_frame = myentry.CourseEntry(master = edit_course_win, title_text="Editing Courses", combobox_values=courses, push_entries=db.commit_courses_info, combobox_command=write_values_from_db)
    entry_frame.pack(padx=(10,10), pady=(20,10))

    # set transparency to 1
    edit_course_win.attributes("-alpha", 1)
    edit_course_win.attributes("-topmost", True)
    edit_course_win.focus_set()
    

def edit_segments():
    
    def write_dates_from_db(segment):
        dates = db.get_segment_info(segment)
        print(dates)
        if dates is None or len(dates) == 0:
            edit_segment_win.focus_set()
            entry_frame.start_dateentry.reset()
            entry_frame.end_dateentry.reset()
            return
        else:
            dates = dates[0][1:]
        print(dates)     
        entry_frame.start_dateentry.write(dates[0])
        entry_frame.end_dateentry.write(dates[1])

    edit_segment_win = ctk.CTkToplevel(fg_color = '#121212')
    
    edit_segment_win.title("Edit Segment Details")
    edit_segment_win.resizable(False, False)
    # set transparency to 0 until window is completely rendered
    edit_segment_win.attributes("-alpha", 0)
    edit_segment_win.update_idletasks()

    edit_segment_win_width=600
    edit_segment_win_height=400
    screen_width=2200
    screen_height=1200
    x_coordinate=int((screen_width/2)-(edit_segment_win_width/2))
    y_coordinate = int((screen_height/2) - (edit_segment_win_height/2))
    edit_segment_win.geometry("{}x{}+{}+{}".format(edit_segment_win_width, edit_segment_win_height, x_coordinate, y_coordinate))

    entry_frame = myentry.SegmentEntry(master=edit_segment_win, push_entries=db.commit_segment_dates, option_menu_cmd=write_dates_from_db)
    write_dates_from_db('1')
    entry_frame.pack(padx=(10,10), pady=(30,30))

    # set transparency to 1
    edit_segment_win.attributes("-alpha", 1)
    edit_segment_win.attributes("-topmost", True)
    edit_segment_win.focus_set()

def clear_timetable(all_slots):
    for btn in all_slots[0]:
        btn.configure(text = 'A')
    for btn in all_slots[1]:
        btn.configure(text = 'B')
    for btn in all_slots[2]:
        btn.configure(text = 'C')
    for btn in all_slots[3]:
        btn.configure(text = 'D')
    for btn in all_slots[4]:
        btn.configure(text = 'E')
    for btn in all_slots[5]:
        btn.configure(text = 'F')
    for btn in all_slots[6]:
        btn.configure(text = 'G')
    for btn in all_slots[7]:
        btn.configure(text = 'P')
    for btn in all_slots[8]:
        btn.configure(text = 'Q')
    for btn in all_slots[9]:
        btn.configure(text = 'R')
    for btn in all_slots[10]:
        btn.configure(text = 'S')
    all_slots[11][0].configure(text = 'FN1')
    all_slots[11][1].configure(text = 'FN2')
    all_slots[11][2].configure(text = 'FN3')
    all_slots[11][3].configure(text = 'FN4')
    all_slots[11][4].configure(text = 'FN5')
    all_slots[12][0].configure(text = 'AN1')
    all_slots[12][1].configure(text = 'AN2')
    all_slots[12][2].configure(text = 'AN3')
    all_slots[12][3].configure(text = 'AN4')
    all_slots[12][4].configure(text = 'AN5')

def change_timetable_to_date(date : tuple[int], all_slots : tuple[tuple[ctk.CTkButton]]):
    date = str(date[0]%100) + '/' + int_2_str(date[1]) + '/' + int_2_str(date[2])
    seg_info = db.get_all_segments_info()
    seg = 1
    for i in seg_info:
        d = i[2]
        d = d[6:] + '/' + d[3:5] + '/' + d[0:2]
        if date > d:
            print(date, d)
            seg += 1
    print(seg)
    courses = db.get_timetable_courses(seg)

    clear_timetable(all_slots)
    for course in courses:
        output_text = course[0] + '\n' + course[1] + '\t' + course[2]
        modify_slot(course[2], output_text, all_slots)
            
def modify_slot(slot, output_text, all_slots):
    match slot:
        case 'A':
            for btn in all_slots[0]:
                btn.configure(text = output_text)
        case 'B':
            for btn in all_slots[1]:
                btn.configure(text = output_text)
        case 'C':
            for btn in all_slots[2]:
                btn.configure(text = output_text)
        case 'D':
            for btn in all_slots[3]:
                btn.configure(text = output_text)
        case 'E':
            for btn in all_slots[4]:
                btn.configure(text = output_text)
        case 'F':
            for btn in all_slots[5]:
                btn.configure(text = output_text)
        case 'G':
            for btn in all_slots[6]:
                btn.configure(text = output_text)
        case 'P':
            for btn in all_slots[7]:
                btn.configure(text = output_text)
        case 'Q':
            for btn in all_slots[8]:
                btn.configure(text = output_text)
        case 'R':
            for btn in all_slots[9]:
                btn.configure(text = output_text)
        case 'S':
            for btn in all_slots[10]:
                btn.configure(text = output_text)
        case 'FN1':
            all_slots[11][0].configure(text = output_text)
        case 'FN2':
            all_slots[11][1].configure(text = output_text)
        case 'FN3':
            all_slots[11][2].configure(text = output_text)
        case 'FN4':
            all_slots[11][3].configure(text = output_text)
        case 'FN5':
            all_slots[11][4].configure(text = output_text)
        case 'AN1':
            all_slots[12][0].configure(text = output_text)
        case 'AN2':
            all_slots[12][1].configure(text = output_text)
        case 'AN3':
            all_slots[12][2].configure(text = output_text)
        case 'AN4':
            all_slots[12][3].configure(text = output_text)
        case 'AN5':
            all_slots[12][4].configure(text = output_text)
    