import customtkinter as ctk
import CTkMenuBar
import CTkDataVisualizingWidgets.CTkDataVisualizingWidgets as dw
import time
import commands
from PIL import Image
from os import path
import sys

def resource_path(relative_path):
    """
    Get absolute path to resource, works for development and pyinstaller
    """
    base_path = getattr(sys, '_MEIPASS', path.abspath("."))
    return path.join(base_path, relative_path)

class Timetable(ctk.CTkFrame):
    A_slot=tuple()
    B_slot=tuple()
    C_slot=tuple()
    D_slot=tuple()
    E_slot=tuple()
    F_slot=tuple()
    G_slot=tuple()
    P_slot=tuple()
    Q_slot=tuple()
    R_slot=tuple()
    S_slot=tuple()
    FN_slot=tuple()
    AN_slot=tuple()

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=50,)
        self.columnconfigure((0,1,2,3,4,5,6,7,8), minsize=50)
        # add widgets onto the frame, for example:
    
    def draw_day_btns(self):
        self.monday_btn = ctk.CTkButton(master=self, width=120, height=80, state='disabled', text="Monday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.tuesday_btn = ctk.CTkButton(master=self, width=120, height=80, state='disabled', text="Tuesday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.wednesday_btn = ctk.CTkButton(master=self, width=120, height=80, state='disabled', text="Wednesday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.thursday_btn = ctk.CTkButton(master=self, width=120, height=80, state='disabled', text="Thursday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.friday_btn = ctk.CTkButton(master=self, width=120, height=80, state='disabled', text="Friday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        # lunch time
        self.lunch_btn = ctk.CTkButton(master=self, width=100, height=440, state='disabled', text="Lunch", corner_radius=0, border_color='#00bfc2', border_width=0.5)

        self.monday_btn.grid(column=0, row = 1, rowspan=2, pady=(0,10), padx=(20,0))
        self.tuesday_btn.grid(column=0, row=3, rowspan=2, pady=(0,10), padx=(20,0))
        self.wednesday_btn.grid(column=0, row=5, rowspan=2, pady=(0,10), padx=(20,0))
        self.thursday_btn.grid(column=0, row=7, rowspan=2, pady=(0,10), padx=(20,0))
        self.friday_btn.grid(column=0, row=9, rowspan=2, pady=(0, 20), padx=(20,0))
        self.lunch_btn.grid(column=5, row=1, rowspan=10, pady=(0,20))
    
    def draw_time_btns(self):
        self.nine_ten_btn = ctk.CTkButton(master=self, width=100, height=50, state='disabled', text="9:00\n9:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.ten_eleven_btn = ctk.CTkButton(master=self, width=100, height=50, state='disabled', text="10:00\n10:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.eleven_twelve_btn = ctk.CTkButton(master=self, width=100, height=50, state='disabled', text="11:00\n11:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.twelve_one_btn = ctk.CTkButton(master=self, width=100, height=50, state='disabled', text="12:00\n12:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.lunch_interval_btn = ctk.CTkButton(master=self, width=100, height=50, state='disabled', text="12:55\n14:30", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.two_thirty_four_btn = ctk.CTkButton(master=self, width=150, height=50, state='disabled', text="14:30\n15:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.four_five_thirty_btn = ctk.CTkButton(master=self, width=150, height=50, state='disabled', text="16:00\n17:25", corner_radius=0, border_color='#00bfc2', border_width=0.5)
        self.six_nine_btn = ctk.CTkButton(master=self, width=300, height=50, state='disabled', text="18:00\n21:00", corner_radius=0, border_color='#00bfc2', border_width=0.5)

        self.nine_ten_btn.grid(column=1, row=0, pady=(20,10))
        self.ten_eleven_btn.grid(column=2, row=0, pady=(20,10))
        self.eleven_twelve_btn.grid(column=3, row=0, pady=(20,10))
        self.twelve_one_btn.grid(column=4, row=0, pady=(20,10))
        self.lunch_interval_btn.grid(column=5, row=0, pady=(20,10))
        self.two_thirty_four_btn.grid(column=6, row=0, pady=(20,10))
        self.four_five_thirty_btn.grid(column=7, row=0, pady=(20,10))
        # self.six_nine_btn.grid(column=8, row=0, pady=(20,10), padx=(0,20))
        # self.six_nine_btn.grid_remove()
    
    def draw_mon_slot_btns(self):
        # monday slots
        self.A_mon_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.B_mon_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.C_mon_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.D_mon_btn = ctk.CTkButton(master=self, width=100, height=80, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.P_mon_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="P", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.Q_mon_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="Q", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.FN1_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="FN1", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.AN1_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="AN1", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

        self.A_mon_btn.grid(column=1, row=1,)
        self.B_mon_btn.grid(column=2, row=1,)
        self.C_mon_btn.grid(column=3, row=1)
        self.D_mon_btn.grid(column=4, row=1, rowspan=2, pady=(0,10))
        self.P_mon_btn.grid(column=6, row=1,)
        self.Q_mon_btn.grid(column=7, row=1,)
        self.FN1_btn.grid(column=1, row=2, columnspan=3, pady=(0,10))
        self.AN1_btn.grid(column=6, row=2, columnspan=2, pady=(0,10))

        Timetable.A_slot += (self.A_mon_btn,)
        Timetable.B_slot += (self.B_mon_btn,)
        Timetable.C_slot += (self.C_mon_btn,)
        Timetable.D_slot += (self.D_mon_btn,)
        Timetable.P_slot += (self.P_mon_btn,)
        Timetable.Q_slot += (self.Q_mon_btn,)
        Timetable.FN_slot += (self.FN1_btn,)
        Timetable.AN_slot += (self.AN1_btn,)
    
    def draw_tue_slot_btns(self):
        self.D_tue_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.E_tue_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.F_tue_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.G_tue_btn = ctk.CTkButton(master=self, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.R_tue_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="R", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.S_tue_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="S", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.FN2_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="FN2", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.AN2_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="AN2", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

        self.D_tue_btn.grid(column=1, row=3,)
        self.E_tue_btn.grid(column=2, row=3,)
        self.F_tue_btn.grid(column=3, row=3)
        self.G_tue_btn.grid(column=4, row=3, rowspan=2, pady=(0,10))
        self.R_tue_btn.grid(column=6, row=3,)
        self.S_tue_btn.grid(column=7, row=3,)
        self.FN2_btn.grid(column=1, row=4, columnspan=3, pady=(0,10))
        self.AN2_btn.grid(column=6, row=4, columnspan=2, pady=(0,10))

        Timetable.D_slot += (self.D_tue_btn,)
        Timetable.E_slot += (self.E_tue_btn,)
        Timetable.F_slot += (self.F_tue_btn,)
        Timetable.G_slot += (self.G_tue_btn,)
        Timetable.R_slot += (self.R_tue_btn,)
        Timetable.S_slot += (self.S_tue_btn,)
        Timetable.FN_slot += (self.FN2_btn,)
        Timetable.AN_slot += (self.AN2_btn,)

    def draw_wed_slot_btns(self):
        self.B_wed_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.C_wed_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.A_wed_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.G_wed_btn = ctk.CTkButton(master=self, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.F_wed_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.FN3_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="FN3", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.AN3_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="AN3/US", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

        self.B_wed_btn.grid(column=1, row=5,)
        self.C_wed_btn.grid(column=2, row=5,)
        self.A_wed_btn.grid(column=3, row=5)
        self.G_wed_btn.grid(column=4, row=5, rowspan=2, pady=(0,10))
        self.F_wed_btn.grid(column=6, row=5,)
        self.FN3_btn.grid(column=1, row=6, columnspan=3, pady=(0,10))
        self.AN3_btn.grid(column=6, row=6, columnspan=2, pady=(0,10))

        Timetable.A_slot += (self.A_wed_btn,)
        Timetable.B_slot += (self.B_wed_btn,)
        Timetable.C_slot += (self.C_wed_btn,)
        Timetable.G_slot += (self.G_wed_btn,)
        Timetable.F_slot += (self.F_wed_btn,)
        Timetable.FN_slot += (self.FN3_btn,)
        Timetable.AN_slot += (self.AN3_btn,)

    def draw_thu_slot_btns(self):
        self.C_thu_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.A_thu_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.B_thu_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.E_thu_btn = ctk.CTkButton(master=self, width=100, height=80, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.Q_thu_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="Q", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.P_thu_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="P", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.FN4_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="FN4", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.AN4_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="AN4", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        # for itp lab & exam
        self.six_nine_thu_btn = ctk.CTkButton(master=self, width=300, height=80, state='normal', text="ITP Exam/Lab", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

        self.C_thu_btn.grid(column=1, row=7,)
        self.A_thu_btn.grid(column=2, row=7,)
        self.B_thu_btn.grid(column=3, row=7)
        self.E_thu_btn.grid(column=4, row=7, rowspan=2, pady=(0,10))
        self.Q_thu_btn.grid(column=6, row=7,)
        self.P_thu_btn.grid(column=7, row=7,)
        self.FN4_btn.grid(column=1, row=8, columnspan=3, pady=(0,10))
        self.AN4_btn.grid(column=6, row=8, columnspan=2, pady=(0,10))
        # self.six_nine_thu_btn.grid(column = 8, row=7, rowspan=2, pady=(0,10), padx=(0,20))
        # self.six_nine_thu_btn.grid_remove()

        Timetable.A_slot += (self.A_thu_btn,)
        Timetable.B_slot += (self.B_thu_btn,)
        Timetable.C_slot += (self.C_thu_btn,)
        Timetable.E_slot += (self.E_thu_btn,)
        Timetable.P_slot += (self.P_thu_btn,)
        Timetable.Q_slot += (self.Q_thu_btn,)
        Timetable.FN_slot += (self.FN4_btn,)
        Timetable.AN_slot += (self.AN4_btn,)

    def draw_fri_slot_btns(self):
        self.E_fri_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.F_fri_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.D_fri_btn = ctk.CTkButton(master=self, width=100, height=40, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.G_fri_btn = ctk.CTkButton(master=self, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.S_fri_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="S", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.R_fri_btn = ctk.CTkButton(master=self, width=150, height=40, state='normal', text="R", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.FN5_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="FN5", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
        self.AN5_btn = ctk.CTkButton(master=self, width=300, height=40, state='normal', text="AN5", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

        self.E_fri_btn.grid(column=1, row=9,)
        self.F_fri_btn.grid(column=2, row=9,)
        self.D_fri_btn.grid(column=3, row=9)
        self.G_fri_btn.grid(column=4, row=9, rowspan=2, pady=(0,20))
        self.S_fri_btn.grid(column=6, row=9,)
        self.R_fri_btn.grid(column=7, row=9,)
        self.FN5_btn.grid(column=1, row=10, columnspan=3, pady=(0,20))
        self.AN5_btn.grid(column=6, row=10, columnspan=2, pady=(0,20))

        Timetable.E_slot += (self.E_fri_btn,)
        Timetable.F_slot += (self.F_fri_btn,)
        Timetable.D_slot += (self.D_fri_btn,)
        Timetable.G_slot += (self.G_fri_btn,)
        Timetable.S_slot += (self.S_fri_btn,)
        Timetable.R_slot += (self.R_fri_btn,)
        Timetable.FN_slot += (self.FN5_btn,)
        Timetable.AN_slot += (self.AN5_btn,)
    
    def create_total_slots_tuple(self):
        self.total_slots = (Timetable.A_slot,
                    Timetable.B_slot,
                    Timetable.C_slot,
                    Timetable.D_slot,
                    Timetable.E_slot,
                    Timetable.F_slot,
                    Timetable.G_slot,
                    Timetable.P_slot,
                    Timetable.Q_slot,
                    Timetable.R_slot,
                    Timetable.S_slot,
                    Timetable.FN_slot,
                    Timetable.AN_slot,
                    )
        
    def write_btn_commands(self, dash, att):
        for i in range(len(self.total_slots)):
            for j in range(len(self.total_slots[i])):
                self.total_slots[i][j]._command = lambda ni=i, nj=j : commands.show_course_details(self.total_slots[ni][nj],
                                                                                                   self.total_slots[ni],
                                                                                                   DashBoard.show_undefined_course_frame,
                                                                                                   DashBoard.show_defined_course_frame,
                                                                                                   dash,
                                                                                                   AttendanceBoard.show_undefined_att_frame,
                                                                                                   AttendanceBoard.show_defined_att_frame,
                                                                                                   att)
    

    def toggle_six_nine_btn(self, value, *args):
        print(value, args)
        if (value.get() == 0):
            self.six_nine_btn.grid_remove()
            self.six_nine_thu_btn.grid_remove()
        else:
            self.six_nine_btn.grid(column=8, row=0, pady=(20,10), padx=(0,20))
            self.six_nine_thu_btn.grid(column = 8, row=7, rowspan=2, pady=(0,10), padx=(0,20))
    
    def refresh_timetable(self, *date):
        commands.change_timetable_to_date(date[::-1], self.total_slots)

class Attendance(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
            

class Tabs(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Timetable")
        self.add("Attendance")

        self.create_timetable()
        self.create_attendance()

    def create_timetable(self):
        self.timetable_frame = Timetable(master=self.tab("Timetable"), width=1200, height=800, border_width=0.5,)
        self.timetable_frame.grid_columnconfigure((0,5,8), pad=30)
        
        self.timetable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew",)

        self.timetable_frame.draw_day_btns()
        self.timetable_frame.draw_time_btns()

        self.timetable_frame.draw_mon_slot_btns()
        self.timetable_frame.draw_tue_slot_btns()
        self.timetable_frame.draw_wed_slot_btns()
        self.timetable_frame.draw_thu_slot_btns()
        self.timetable_frame.draw_fri_slot_btns()

        self.timetable_frame.create_total_slots_tuple()
    
    def create_attendance(self):
        self.attendance_frame = Attendance(master=self.tab("Attendance"), width=990, height=525, border_width=0.5,)
        self.attendance_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

class MenuBar():
    def __init__(self, master, **kwargs):
        self.master=master
        self.menu = CTkMenuBar.CTkMenuBar(master=self.master)

        self.file_button = self.menu.add_cascade("File")
        self.edit_button = self.menu.add_cascade("Edit")
        self.options_button = self.menu.add_cascade("Options")
        self.help_button = self.menu.add_cascade("About")

    def adjust_transparency(self, value : float):
        self.master.attributes("-alpha", value)
    
    def make_file_dropdown(self):
        self.file_dropdown = CTkMenuBar.CustomDropdownMenu(widget = self.file_button, separator_color='white')
        self.file_dropdown.add_option(option = "Export", command = commands.export_calendar_file)
        self.file_dropdown.add_separator()
        self.file_dropdown.add_option(option = "Exit", command = self.master.destroy)
    
    def make_edit_dropdown(self):
        self.edit_dropdown = CTkMenuBar.CustomDropdownMenu(widget = self.edit_button, separator_color='white')
        
        self.edit_dropdown.add_option(option = "Upload Academic Timetable", command=commands.upload_tt)
        self.edit_dropdown.add_separator()
        self.edit_dropdown.add_option(option = "Edit Segments", command=commands.edit_segments)
        self.edit_dropdown.add_option(option = "Edit Holidays", command=commands.edit_holidays)
        self.edit_dropdown.add_option(option = "Edit Courses", command=commands.edit_courses)
    
    def make_options_dropdown(self):
        self.options_dropdown = CTkMenuBar.CustomDropdownMenu(widget = self.options_button)
        self.options_dropdown.add_option(option="Adjust Transparency", state = 'disabled')

        self.transparency_slider=ctk.CTkSlider(
                                    master=self.options_dropdown,
                                    from_=0,
                                    to=1,
                                    state='normal',
                                    orientation="horizontal",
                                    command=self.adjust_transparency,
                                    width=100,
                                )
        self.transparency_slider.set(0.92)
        self.transparency_slider.pack(pady=(0,10), padx=(10,10), anchor='center', fill='x')
        self.check_var = ctk.IntVar(value=0)
        self.six_nine_check = ctk.CTkCheckBox(
                                    master=self.options_dropdown,
                                    text = "Six to Nine Button",
                                    hover=True,
                                    variable=self.check_var,
                                )        
        self.six_nine_check.pack(pady=(10,10), padx=(10,10), anchor='center', fill='x')
        self.options_dropdown.add_option(option = "Reset Database", command=commands.reset_db)
        self.options_dropdown.theme_menu = self.options_dropdown.add_submenu("Change Theme")
        self.options_dropdown.theme_menu.add_option(option = "Default", command=lambda: change_theme("default"))
        self.options_dropdown.theme_menu.add_option(option = "Printable", command=lambda: change_theme("to_print"))
        self.options_dropdown.theme_menu.add_option(option = "Sweetkind", command=lambda: change_theme("sweetkind"))
    
    def make_help_dropdown(self):        
        self.help_dropdown = CTkMenuBar.CustomDropdownMenu(widget=self.help_button)
        self.help_dropdown.add_option(option = "View on Github", command = commands.open_source_code)

    def make_all_dropdowns(self):
        self.make_file_dropdown()
        self.make_edit_dropdown()
        self.make_options_dropdown()
        self.make_help_dropdown()
    
class DashBoard(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), minsize=50)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,), minsize=50)
        
        self.header_label = ctk.CTkLabel(master=self, text="Dashboard", font=("Helvetica", 24))
        self.header_label.grid(row=0, column=0, columnspan=15, padx=(10,10), pady=(20,10))

        self.calendar = dw.ctk_calender.CTkCalendar(master=self, width=300, height=300, calendar_btns_pad=3, today_fg_color="black", date_highlight_color="green", border_width=0.6)
        self.calendar.grid(row=1, column=0, columnspan=15, padx=(10,10), pady=(10,10))

        self.course_details_label = ctk.CTkLabel(master=self, text="Course Details", font=("Helvetica", 22))
        self.course_details_label.grid(row=3, column=0, columnspan = 15, padx=(10,10), pady=(10,10))

        self.define_ud_course_frame()
        self.define_d_course_frame()
    
    def define_ud_course_frame(self):
        self.ud_course_frame = ctk.CTkFrame(master=self, border_width=1)
        self.ud_course_frame.grid_columnconfigure((0,1,2,3,4), minsize=50)
        self.ud_course_frame.label = ctk.CTkLabel(master=self.ud_course_frame, text = "Slot not Defined", font=("Helvetica", 20))
        self.ud_course_frame.label.grid(row=0, column = 0, columnspan = 5, padx=(5,5), pady=(5,5))

    def define_d_course_frame(self):
        self.d_course_frame  = ctk.CTkFrame(master=self, width=300, height=300, border_width=1)
        self.d_course_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), minsize=25)
        self.d_course_frame.grid_rowconfigure((0,1,2,3,4,5), minsize=50)
        
        self.d_course_frame.c_title = ctk.CTkLabel(master=self.d_course_frame, text="Course Title")
        self.d_course_frame.c_code  = ctk.CTkLabel(master=self.d_course_frame, text="Course Code")
        self.d_course_frame.c_venue = ctk.CTkLabel(master=self.d_course_frame, text="Course Venue")
        self.d_course_frame.s_start = ctk.CTkLabel(master=self.d_course_frame, text="Start Segment")
        self.d_course_frame.to_label  = ctk.CTkLabel(master=self.d_course_frame, text="to")
        self.d_course_frame.s_end   = ctk.CTkLabel(master=self.d_course_frame, text="End Segment")
        self.d_course_frame.slot_text = ctk.CTkLabel(master=self.d_course_frame, text="Slot Text")
        self.d_course_frame.slot    = ctk.CTkLabel(master=self.d_course_frame, text="Slot")

        self.d_course_frame.c_title.grid(row=0, column=0, columnspan=10, padx=(10,10), pady=(10,10))
        self.d_course_frame.c_code.grid(row=2, column=0, columnspan=2, padx=(10,0), pady=(10,10))
        self.d_course_frame.s_start.grid(row=2, column=3, columnspan=2, padx=(10,0), pady=(10,10))
        self.d_course_frame.to_label.grid(row=3, column=5, columnspan=1, padx=(10,0), pady=(0,10))
        self.d_course_frame.s_end.grid(row=2, column=6, columnspan=2, padx=(10,10), pady=(10,10))
        self.d_course_frame.c_venue.grid(row=4, column=0, columnspan=2, padx=(10,0), pady=(10,10))
        self.d_course_frame.slot_text.grid(row=4, column=3, columnspan=2, padx=(10,0), pady=(10,10))
        self.d_course_frame.slot.grid(row=4, column=6, columnspan=2, padx=(10,10), pady=(10,10))

        self.d_course_frame.c_title_text = ctk.CTkTextbox(master=self.d_course_frame, width=350, height=28, font=("Helvetica", 20), wrap='none', border_spacing=3)
        self.d_course_frame.c_code_text  = ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.d_course_frame.c_venue_text = ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.d_course_frame.s_start_text = ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.d_course_frame.s_end_text   = ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.d_course_frame.slot_text_text=ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.d_course_frame.slot_textt   = ctk.CTkTextbox(master=self.d_course_frame, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)

        self.d_course_frame.text_boxes = (self.d_course_frame.c_title_text,
                                          self.d_course_frame.c_code_text,
                                          self.d_course_frame.c_venue_text,
                                          self.d_course_frame.s_start_text,
                                          self.d_course_frame.s_end_text,
                                          self.d_course_frame.slot_text_text,
                                          self.d_course_frame.slot_textt,
                                          )
        
        for tb in self.d_course_frame.text_boxes:
            tb.tag_config('center', justify='center')
            tb.insert('end', "Click a Course", 'center')
            if tb.xview() != (0.0, 1.0):
                tb.delete('1.0', 'end')
                tb.insert('end', "Click a Course")
            tb.configure(state='disabled')

        self.d_course_frame.c_title_text.grid(row=1, column=0, columnspan=10, padx=(10,10), pady=(0,10))
        self.d_course_frame.c_code_text.grid(row=3, column=0, columnspan=2, padx=(10,0), pady=(0,10))
        self.d_course_frame.s_start_text.grid(row=3, column=3, columnspan=2, padx=(10,0), pady=(0,10))
        self.d_course_frame.s_end_text.grid(row=3, column=6, columnspan=2, padx=(10,10), pady=(0,10))
        self.d_course_frame.c_venue_text.grid(row=5, column=0, columnspan=2, padx=(10,0), pady=(0,10))
        self.d_course_frame.slot_text_text.grid(row=5, column=3, columnspan=2, padx=(10,0), pady=(0,10))
        self.d_course_frame.slot_textt.grid(row=5, column=6, columnspan=2, padx=(10,10), pady=(0,10))
        
        self.d_course_frame.grid(row=4, column=0, columnspan=15, padx=(10,10), pady=(10,20))     

    def show_undefined_course_frame(self, slot : str):
        self.ud_course_frame.label.configure(text = f'{slot} is not defined')
        self.d_course_frame.grid_remove()
        self.ud_course_frame.grid(row=4, column=0, columnspan=15, padx=(10,10), pady=(10,10))
    
    def show_defined_course_frame(self, args):        
        args = args[0]
        for tb, text in zip(self.d_course_frame.text_boxes, args):
            tb.configure(state='normal')
            tb.delete('1.0', 'end')
            tb.insert('end', text, 'center')
            if tb.xview() != (0.0, 1.0):
                tb.delete('1.0', 'end')
                tb.insert('end', text)
            tb.configure(state='disabled')

        self.ud_course_frame.grid_remove()
        self.d_course_frame.grid(row=4, column=0, columnspan=15, padx=(10,10), pady=(10,20))

class AttendanceBoard(ctk.CTkFrame):
    add_img = ctk.CTkImage(Image.open(resource_path("icons/add.png")), size = (30,30))
    sub_img = ctk.CTkImage(Image.open(resource_path("icons/subtract.png")), size = (30,30))

    def __init__(self, master, width=1075, height=300, **kwargs):
        super().__init__(master, width, height, **kwargs)
        self.columnconfigure((0,1,2,3,4,5,6), minsize=100)
        self.rowconfigure((0,1,2,3,4,5,6,7,8), minsize=50)

        self.att = ctk.Variable(value=0.75)
        self.att_per = ctk.Variable(value='75 %')
        self.w_days = ctk.Variable(value="Click a Course")
        self.textboxes : list[ctk.CTkTextbox] = []
        self.checkboxes : list[ctk.CTkCheckBox] = []

        # input label
        self.input_label = ctk.CTkLabel(master=self, text="Set Required Attendance", font=("Helvetica", 22))
        self.input_label.grid(row=0, column=0, columnspan=4, padx=(10,10), pady=(10,0))
        
        # subtract att button
        self.sub_btn = ctk.CTkButton(master=self, image=self.sub_img, width=0, height=0, fg_color='transparent', border_width=0, text = "", corner_radius=100, hover=False, command=self.decrease_att, state='disabled')
        self.sub_btn.grid(row=1, column=0, padx=(10,10), pady=(10,0))
        
        # att slider
        self.att_slider = ctk.CTkSlider(master=self, width=200, from_=0, to=1, number_of_steps=100, variable=self.att, command=self.change_att, state='disabled')
        self.att_slider.grid(row=1, column=1 ,columnspan=2, pady=(10,0))
    
        # add att button
        self.add_btn = ctk.CTkButton(master=self, image=self.add_img, width=0, height=0, fg_color='transparent', border_width=0, text = "", corner_radius=100, hover=False, command=self.increase_att, state='disabled')
        self.add_btn.grid(row=1, column=3, padx=(10,10), pady=(10,0))

        # att pecentage label
        self.att_per_label = ctk.CTkLabel(master=self, textvariable=self.att_per, font=("Helvetica", 14))
        self.att_per_label.grid(row=2, column=1, columnspan=2, pady=(0,0))

        # no of working days label
        self.no_working_days_label = ctk.CTkLabel(master=self, text="No. of Working Days", font=("Helvetica", 18))
        self.no_working_days_label.grid(row=3, column=0, columnspan=2, padx=(10,10), pady=(10,0))

        # w_days textbox
        self.w_days_text = ctk.CTkTextbox(master=self, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.w_days_text.grid(row=4, column=0, columnspan=2, padx=(10,10), pady=(10,0))

        # bunkable label
        self.bunk_label = ctk.CTkLabel(master=self, text="Can Bunk", font=("Helvetica", 18))
        self.bunk_label.grid(row=3, column=2, columnspan=2, padx=(10,10), pady=(10,0))

        # bunk textbox
        self.bunk_days_text = ctk.CTkTextbox(master=self, width=100, height=28, font=("Helvetica", 16), wrap='none', border_spacing=3)
        self.bunk_days_text.grid(row=4, column=2, columnspan=2, padx=(10,10), pady=(10,0))

        # divider frame
        self.divider_frame = ctk.CTkFrame(master=self, border_color='#00bfc2', border_width=1, width=2, bg_color='#00bfc2', fg_color='#00bfc2')
        self.divider_frame.grid(row=0, column=4, rowspan=7, sticky='ns', pady=(0,0))

        # working days label
        self.working_days_label = ctk.CTkLabel(master=self, text="Course Working Days", font=("Helvetica", 22))
        self.working_days_label.grid(row=0, column=5, columnspan=3, padx=(0,20), pady=(10,0))

        self.dow_frame = ctk.CTkFrame(master=self, fg_color='#23272D')
        self.dow_frame.grid(row=1, column=5, rowspan=5, columnspan=3, padx=(10,10), pady=(10,0))

        # days of the week
        self.mon_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Monday")
        self.tue_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Tuesday")
        self.wed_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Wednesday")
        self.thu_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Thursday")
        self.fri_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Friday")
        self.sat_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Saturday")
        self.sun_check = ctk.CTkCheckBox(master=self.dow_frame, font=("Helvetica", 16), state='disabled', text="Sunday")

        self.mon_check.grid(row=0, column=4, columnspan=3, padx=(10,10), pady=(10,0), sticky='w')
        self.tue_check.grid(row=1, column=4, columnspan=3, padx=(10,10), pady=(5,0), sticky='w')
        self.wed_check.grid(row=2, column=4, columnspan=3, padx=(10,10), pady=(5,0), sticky='w')
        self.thu_check.grid(row=3, column=4, columnspan=3, padx=(10,10), pady=(5,0), sticky='w')
        self.fri_check.grid(row=4, column=4, columnspan=3, padx=(10,10), pady=(5,0), sticky='w')
        self.sat_check.grid(row=5, column=4, columnspan=3, padx=(10,10), pady=(5,0), sticky='w')
        self.sun_check.grid(row=6, column=4, columnspan=3, padx=(10,10), pady=(5,10), sticky='w')

        self.checkboxes.append(self.mon_check)
        self.checkboxes.append(self.tue_check)
        self.checkboxes.append(self.wed_check)
        self.checkboxes.append(self.thu_check)
        self.checkboxes.append(self.fri_check)
        self.checkboxes.append(self.sat_check)
        self.checkboxes.append(self.sun_check)

        self.textboxes.append(self.w_days_text)
        self.textboxes.append(self.bunk_days_text)
        for tb in self.textboxes:
            tb.tag_config('center', justify='center')
            tb.insert('end', "Click a Course", 'center')
            if tb.xview() != (0.0, 1.0):
                tb.delete('1.0', 'end')
                tb.insert('end', "Click a Course")
            tb.configure(state='disabled')

    def att_2_att_per(self):
        self.att_per.set(str(int(self.att.get()*100))+' %')
    
    def change_att(self, *args):
        self.att_2_att_per()
        commands.change_att_of_highlighted_course(self.att.get(), self.show_defined_att_frame, self)
    
    def decrease_att(self):
        if self.att.get() <= 0 :
            self.att.set(0)
        else:
            self.att.set(self.att.get()-0.01)
        self.change_att()
    
    def increase_att(self):
        if self.att.get() >= 1:
            self.att.set(1)
        else:
            self.att.set(self.att.get()+0.01)
        self.change_att()
        
    def show_undefined_att_frame(self, slot):
        self.att_slider.configure(state='disabled')
        self.add_btn.configure(state='disabled')
        self.sub_btn.configure(state='disabled')
        for tb in self.textboxes:
            tb.configure(state='normal')
            tb.tag_config('center', justify='center')
            tb.insert('end', f"{slot} is not defined", 'center')
            if tb.xview() != (0.0, 1.0):
                tb.delete('1.0', 'end')
                tb.insert('end', f"{slot} is not defined")
            tb.configure(state='disabled')    
        
        for cb in self.checkboxes:
            cb.deselect()
            cb.configure(state='disabled')
    
    def show_defined_att_frame(self, *args):
        # print(args)
        self.att_slider.configure(state='normal')
        self.add_btn.configure(state='normal')
        self.sub_btn.configure(state='normal')
        for cb in self.checkboxes:
            cb.configure(state='normal')

        for tb, text in zip(self.textboxes, args[:2]):
            tb.configure(state='normal')
            tb.delete('1.0', 'end')
            tb.insert('end', text, 'center')
            if tb.xview() != (0.0, 1.0):
                tb.delete('1.0', 'end')
                tb.insert('end', text)
            tb.configure(state='disabled')
        
        # select the working days only
        for i in range(0,7):
            if i in args[-1]:
                self.checkboxes[i].select()
            else:
                self.checkboxes[i].deselect()
                self.checkboxes[i].configure(state='disabled')


class App(ctk.CTk):
    current_time=time.localtime()
    def __init__(self):
        self.theme = 'default' if commands.db.get_theme() == [] else commands.db.get_theme()[0][0]
        if self.theme == 'to_print':
            ctk.set_appearance_mode('light')
        else:
            ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme(resource_path("themes/"+self.theme+".json"))
        super().__init__()
        self.geometry(f'{str(self.winfo_screenwidth())}x{str(self.winfo_screenheight())}')
        self.title("Timetable") # window title
        self.after(5, lambda: self.state("zoomed")) # set to fullscreen
        self.attributes("-alpha", 0.92)

        self.menubar = MenuBar(master=self)
        self.menubar.make_all_dropdowns()
        self.menubar.six_nine_check._command = lambda value=self.menubar.six_nine_check._variable: self.my_tabs.timetable_frame.toggle_six_nine_btn(value)

        self.dash = DashBoard(master = self, border_width=1)
        self.dash.pack(padx=(20,20), pady=(28,10), side='left', anchor='nw')

        self.my_tabs = Tabs(master=self, border_width=1)
        # self.my_tabs.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky='nsew')
        self.my_tabs.pack(padx=(10,10), pady=(10,10), anchor='center')

        self.dash.calendar.calendar_dates_command = self.my_tabs.timetable_frame.refresh_timetable
        self.my_tabs.timetable_frame.refresh_timetable(App.current_time.tm_mday, App.current_time.tm_mon, App.current_time.tm_year)

        self.att_board = AttendanceBoard(master=self, border_width=1)
        self.att_board.pack(side='left', padx=(65,0), pady=(20,20))

        self.my_tabs.timetable_frame.write_btn_commands(self.dash, self.att_board)

def change_theme(to : str):
    commands.confirmation_win("App will have to be restarted manually", y_cmd= lambda: commands.db.commit_theme(to), restart=True)

# app = App()
# print(App.current_time)

# app.mainloop()
