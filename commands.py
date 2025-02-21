import customtkinter as ctk
import CTkMessagebox
import os
import db
import myentry
import read_pdf
from datetime import date, timedelta

highlighted_btns = None

def int_2_str(n : int):
    """
    Returns string of given integer. 9 is returned as 09
    """
    if (n//10 == 0):
        return '0' + str(n)
    else:
        return str(n)

def dd_mm_yy_2_yy_mm_dd(date : str, delimiter = '/'):
    date = date.split(delimiter)[::-1]
    return delimiter.join(date)

def date_2_int(date : str, delimiter='/'):
    return int(date.replace(delimiter, ''))

def days_between(start : str, end : str, inclusive : bool = True):
    """
    Assuming date is passed as DD/MM/YY
    """
    # convert to YY/MM/DD
    # convert to YY/MM/DD
    s=int(dd_mm_yy_2_yy_mm_dd(start).replace('/', ''))
    e=int(dd_mm_yy_2_yy_mm_dd(end).replace('/', ''))
    
    return e - s + inclusive

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

def upload_tt():

    def kill_win_n_push_dates(win : ctk.CTkToplevel, dates_dict : dict, hols_dict : dict):
        for seg, dates in dates_dict.items():
            if seg.isdigit() == False:
                # semester break
                db.commit_holiday(seg, dates, days_between(dates[0], dates[1]))
            db.commit_segment_dates(seg, dates[0], dates[1])
        for hol, date in hols_dict.items():
            print(date)
            db.commit_holiday(hol, date)
        win.destroy()

    def kill_win_n_edit_dates(win : ctk.CTkToplevel, dates_dict : dict, hols_dict : dict):
        win.destroy()
        edit_segments(dates_dict)
        edit_holidays(hols_dict)

    f_path = ctk.filedialog.askopenfilename(initialdir=os.getcwd(), title="Choose File", filetypes=[("PDF Files", ".pdf")])
    tb = read_pdf.TT_Pdf(file_path=f_path)

    confirm_win = ctk.CTkToplevel(fg_color='#121212')
    confirm_win.title("Confirm Segment Details")
    confirm_win.resizable(False, False)
    confirm_win.attributes('-alpha', 0)
    confirm_win.update_idletasks()

    confirm_win_width=400
    confirm_win_height=500
    screen_width=2200
    screen_height=1200
    x_coordinate=int((screen_width/2)-(confirm_win_width/2))
    y_coordinate = int((screen_height/2) - (confirm_win_height/2))
    confirm_win.geometry("{}x{}+{}+{}".format(confirm_win_width, confirm_win_height, x_coordinate, y_coordinate))

    ctk.CTkLabel(master=confirm_win, text="Confirm Segment Dates", font=("Helvetica", 22)).pack(side='top', pady=(30,10), fill='x')

    frame = ctk.CTkScrollableFrame(master=confirm_win, width=300, height=300, border_color='white', border_width=0.5)
    frame.pack(padx=(10,10), pady=(30, 10), fill = 'y')
    frame.grid_columnconfigure((0,1,2), minsize = 50)
    frame.grid_rowconfigure((0,1,2,3,4,5,6), minsize=50)

    ctk.CTkLabel(master=frame, text="Start").grid(row=0, column=1, padx=(0,10), pady=(10,10))
    ctk.CTkLabel(master=frame, text="End").grid(row=0, column=2, padx=(0,10), pady=(10,10))

    for seg, dates, row in zip(tb.d_dates.keys(), tb.d_dates.values(), range(1,8)):
        ctk.CTkLabel(master=frame, text=seg).grid(row=row, column=0, padx=(10,10), pady=(0,10))
        ctk.CTkLabel(master=frame, text=dates[0]).grid(row=row, column=1, padx=(10,10), pady=(0,10))
        ctk.CTkLabel(master=frame, text=dates[1]).grid(row=row, column=2, padx=(10,10), pady=(0,10))
    
    ctk.CTkLabel(master=frame, text="Holidays").grid(row=8, column=1, padx=(10,10), pady=(10,10))

    for name, date, row in zip(tb.holidays.keys(), tb.holidays.values(), range(9,9+len(tb.holidays))):
        ctk.CTkLabel(master=frame, text=name).grid(row=row, column=0, padx=(10,10), pady=(0,10))
        ctk.CTkLabel(master=frame, text=date).grid(row=row, column=2, padx=(10,10), pady=(0,10))
    
    ctk.CTkButton(master=confirm_win, text="Edit Dates", command= lambda w=confirm_win, d=tb.d_dates, h=tb.holidays: kill_win_n_edit_dates(w, d, h)).pack(side='left', padx=(10,10), pady=(10,10))
    ctk.CTkButton(master=confirm_win, text="OK", command= lambda w=confirm_win, d=tb.d_dates, h=tb.holidays: kill_win_n_push_dates(w, d, h)).pack(side='right', padx=(10,10), pady=(10,10))

    confirm_win.attributes('-alpha', 1)

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
    
def edit_holidays(values = None):
    
    def write_dates_from_values():
        entry_frame._values_entries_dict = values
        entry_frame._option_menu_values = list(values.keys())
        entry_frame.option_menu.configure(list(values.keys()))
        entry_frame.set_entries_to(entry_frame._option_menu_values[0])

    def write_dates_from_db():
        data = db.get_all_holidays_info()
        d = {}
        for i in data:
            if i[0].lower() == 'sem_break':
                continue
            d[i[0]] = i[1]
        entry_frame._values_entries_dict = d
        entry_frame._option_menu_values = list(d.keys())
        entry_frame.option_menu.configure(values = list(d.keys()))
        entry_frame.set_entries_to(entry_frame._option_menu_values[0])

    opt_cmd = write_dates_from_db if values is None else write_dates_from_values
    edit_hol_win = ctk.CTkToplevel(fg_color = '#121212')
    
    edit_hol_win.title("Edit Course Details")
    edit_hol_win.resizable(False, False)
    # set transparency to 0 until window is completely rendered
    edit_hol_win.attributes("-alpha", 0)
    edit_hol_win.update_idletasks()

    edit_hol_win_width=600
    edit_hol_win_height=425
    screen_width=2200
    screen_height=1200
    x_coordinate=int((screen_width/2)-(edit_hol_win_width/2))
    y_coordinate = int((screen_height/2) - (edit_hol_win_height/2))
    edit_hol_win.geometry("{}x{}+{}+{}".format(edit_hol_win_width, edit_hol_win_height, x_coordinate, y_coordinate))

    entry_frame = myentry.HoldidayEntry(master=edit_hol_win, push_entries=db.commit_holiday)
    opt_cmd()
    entry_frame.pack(padx=(10,10), pady=(30,30))

    edit_hol_win.attributes('-alpha', 1)
    edit_hol_win.attributes("-topmost", True)
    edit_hol_win.focus_set()

def edit_segments(values = None):
    
    def write_dates_from_values(segment):
        entry_frame.start_dateentry.write(values[segment][0])
        entry_frame.end_dateentry.write(values[segment][1])
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
        # print(dates)
        entry_frame.start_dateentry.write(dates[0])
        entry_frame.end_dateentry.write(dates[1])
    opt_cmd = write_dates_from_db if values is None else write_dates_from_values
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

    entry_frame = myentry.SegmentEntry(master=edit_segment_win, push_entries=db.commit_segment_dates, option_menu_cmd=opt_cmd)
    opt_cmd('1')
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
    print(seg_info)
    seg = 1
    for i in seg_info:
        d = i[2]
        d = d[6:] + '/' + d[3:5] + '/' + d[0:2]
        if date > d:
            print(date, d)
            seg += 1
    # print(seg)
    courses = db.get_timetable_courses(seg)

    clear_timetable(all_slots)
    for course in courses:
        output_text = course[0] + '\n' + course[1] + '\t' + course[2]
        # slot is course[2]]
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
    
def show_course_details(btn : ctk.CTkButton, btns : tuple[ctk.CTkButton], show_undefined, show_defined, dashboard):
    global highlighted_btns

    btn_text : str = btn.cget("text")
    s_text = btn_text.split('\n')[0]
    s = btn_text.split('\t')[-1]
    if len(btn_text) == 1 or len(btn_text) == 3:
        show_undefined(dashboard, s)
    else:
        show_defined(dashboard, db.get_course_info_from_slot(s_text, s))
    
    if highlighted_btns is not None:
        for x in highlighted_btns:
            x.configure(border_color = "#00bfc2", border_width = 0.5)

    if len(btns) == 5:
        btn.configure(border_color = 'orange', border_width = 1)
        highlighted_btns = (btn,)
    else:
        for btn1 in btns:
            btn1.configure(border_color = 'orange', border_width = 1)
        highlighted_btns = btns

def create_hols_list():
    hols_info = db.get_all_holidays_info()
    hols = []
    for row in hols_info:
        if row[-1] > 1:
            start = dd_mm_yy_2_yy_mm_dd(row[1]).split('/')
            end = dd_mm_yy_2_yy_mm_dd(row[2]).split('/')
            start = date(2000+int(start[0]), int(start[1]), int(start[2]))
            end = date(2000+int(end[0]), int(end[1]), int(end[2]))
            hols.extend([(start+timedelta(days=x)).strftime("%d/%m/%y") for x in range(((end + timedelta(days=1))-start).days)])
        else:
            hols.append(row[1])
    return hols