import customtkinter as ctk
import CTkMenuBar
import CTkListbox
import CTkMessagebox
import time
import commands

# create main window
app = ctk.CTk(fg_color='#121212')
app.geometry(f'{str(app.winfo_screenwidth())}x{str(app.winfo_screenheight())}')
app.title("Timetable") # window title
ctk.set_appearance_mode("dark") # dark mode 
app.after(5, lambda: app.state("zoomed")) # set to fullscreen

def initialize_app():
    # get transparency
    transparency=0.92
    # set application's transparency to above transparency
    app.attributes('-alpha', transparency)
    # get scaling factor
    scale_factor=2560/app.winfo_screenwidth()
    # get current time
    current_time=time.localtime()
    
    # make dictionary of items to return
    d={'transparency': transparency, 
       'scale_factor': scale_factor, 
       'current_time': current_time,
       }
    return d

initialized_items=initialize_app()

def adjust_transparency(value):
    '''
    Sets transparency to given value. 
    Stored in dict of initialized items
    '''
    app.attributes('-alpha', value)
    initialized_items['transparency']=value

menu = CTkMenuBar.CTkMenuBar(app)
menu.lift()

# add buttons for different commands
file_button = menu.add_cascade("File")
edit_button = menu.add_cascade("Edit")
options_button = menu.add_cascade("Options")
help_button = menu.add_cascade("Help")

""" Dropdown for respective subcommands """

# file cascade
file_dropdown = CTkMenuBar.CustomDropdownMenu(widget = file_button)
file_dropdown.add_option(option = "Open", command = commands.open_calendar_file)
file_dropdown.add_separator()
file_dropdown.add_option(option = "Exit", command = app.destroy)

# options cascade
options_dropdown = CTkMenuBar.CustomDropdownMenu(widget = options_button)
options_dropdown.add_option(option="Adjust Transparency", state = 'disabled')

transparency_slider=ctk.CTkSlider(
    master=options_dropdown,
    from_=0,
    to=1,
    state='normal',
    # progress_color=initialized_items['current_theme']["color3"],
    # button_color=initialized_items['current_theme']["color4"],
    # button_hover_color=initialized_items['current_theme']["color5"],
    orientation="horizontal",
    command=adjust_transparency,
    width=100,
)
transparency_slider.set(initialized_items["transparency"])
transparency_slider.pack(pady=(0,10), padx=(10,10), anchor='center', fill='x')

# help cascade
help_dropdown = CTkMenuBar.CustomDropdownMenu(widget=help_button)
help_dropdown.add_option(option = "About", command = commands.open_source_code)


# main frame
main_frame = ctk.CTkFrame(
    master = app,
    height = 800,
    width = 1200,
    corner_radius = 20,
    fg_color='#151F36',
    border_width=0.5,
    border_color='#00bfc2',
)
main_frame.pack(anchor = 'center', padx = (10,10), pady=(30,30), ipadx = 50, ipady = 20)
main_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),  minsize=150,)
main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), minsize=50,)
main_frame.grid_columnconfigure((0,5,8), pad=30)
# main_frame.grid_rowconfigure((0,2,4,6,8,10), pad=30)

# define time intervals
nine_ten_btn = ctk.CTkButton(master=main_frame, width=100, height=50, state='disabled', text="9:00\n9:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
ten_eleven_btn = ctk.CTkButton(master=main_frame, width=100, height=50, state='disabled', text="10:00\n10:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
eleven_twelve_btn = ctk.CTkButton(master=main_frame, width=100, height=50, state='disabled', text="11:00\n11:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
twelve_one_btn = ctk.CTkButton(master=main_frame, width=100, height=50, state='disabled', text="12:00\n12:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
lunch_interval_btn = ctk.CTkButton(master=main_frame, width=100, height=50, state='disabled', text="12:55\n14:30", corner_radius=0, border_color='#00bfc2', border_width=0.5)
two_thirty_four_btn = ctk.CTkButton(master=main_frame, width=150, height=50, state='disabled', text="14:30\n15:55", corner_radius=0, border_color='#00bfc2', border_width=0.5)
four_five_thirty_btn = ctk.CTkButton(master=main_frame, width=150, height=50, state='disabled', text="16:00\n17:25", corner_radius=0, border_color='#00bfc2', border_width=0.5)
six_nine_btn = ctk.CTkButton(master=main_frame, width=300, height=50, state='disabled', text="18:00\n21:00", corner_radius=0, border_color='#00bfc2', border_width=0.5)

nine_ten_btn.grid(column=1, row=0, pady=10)
ten_eleven_btn.grid(column=2, row=0, pady=10)
eleven_twelve_btn.grid(column=3, row=0, pady=10)
twelve_one_btn.grid(column=4, row=0, pady=10)
lunch_interval_btn.grid(column=5, row=0, pady=10)
two_thirty_four_btn.grid(column=6, row=0, pady=10)
four_five_thirty_btn.grid(column=7, row=0, pady=10)
six_nine_btn.grid(column=8, row=0, pady=10)

# define weekdays buttons
monday_btn = ctk.CTkButton(master=main_frame, width=120, height=80, state='disabled', text="Monday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
tuesday_btn = ctk.CTkButton(master=main_frame, width=120, height=80, state='disabled', text="Tuesday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
wednesday_btn = ctk.CTkButton(master=main_frame, width=120, height=80, state='disabled', text="Wednesday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
thursday_btn = ctk.CTkButton(master=main_frame, width=120, height=80, state='disabled', text="Thursday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
friday_btn = ctk.CTkButton(master=main_frame, width=120, height=80, state='disabled', text="Friday", corner_radius=0, border_color='#00bfc2', border_width=0.5)
# lunch time
lunch_btn = ctk.CTkButton(master=main_frame, width=100, height=440, state='disabled', text="Lunch", corner_radius=0, border_color='#00bfc2', border_width=0.5)

monday_btn.grid(column=0, row = 1, rowspan=2, pady=(0,10))
tuesday_btn.grid(column=0, row=3, rowspan=2, pady=(0,10))
wednesday_btn.grid(column=0, row=5, rowspan=2, pady=(0,10))
thursday_btn.grid(column=0, row=7, rowspan=2, pady=(0,10))
friday_btn.grid(column=0, row=9, rowspan=2, pady=(0,10))
lunch_btn.grid(column=5, row=1, rowspan=10, pady=(0,10))

'''Classes Buttons (Slots A, B, C, etc...)'''

# monday slots
A_mon_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
B_mon_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
C_mon_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
D_mon_btn = ctk.CTkButton(master=main_frame, width=100, height=80, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
P_mon_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="P", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
Q_mon_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="Q", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
FN1_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="FN1", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
AN1_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="AN1", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

# tuesday slots
D_tue_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
E_tue_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
F_tue_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
G_tue_btn = ctk.CTkButton(master=main_frame, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
R_tue_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="R", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
S_tue_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="S", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
FN2_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="FN2", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
AN2_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="AN2", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

# wednesday slots
B_wed_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
C_wed_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
A_wed_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
G_wed_btn = ctk.CTkButton(master=main_frame, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
F_wed_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
FN3_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="FN3", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
AN3_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="AN3/US", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

# thursday slots
C_thu_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="C", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
A_thu_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="A", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
B_thu_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="B", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
E_thu_btn = ctk.CTkButton(master=main_frame, width=100, height=80, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
Q_thu_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="Q", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
P_thu_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="P", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
FN4_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="FN4", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
AN4_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="AN4", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
# for itp lab & exam
six_nine_thu_btn = ctk.CTkButton(master=main_frame, width=300, height=80, state='normal', text="ITP Exam/Lab", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

# friday slots
E_fri_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="E", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
F_fri_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="F", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
D_fri_btn = ctk.CTkButton(master=main_frame, width=100, height=40, state='normal', text="D", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
G_fri_btn = ctk.CTkButton(master=main_frame, width=100, height=80, state='normal', text="G", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
S_fri_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="S", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
R_fri_btn = ctk.CTkButton(master=main_frame, width=150, height=40, state='normal', text="R", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
FN5_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="FN5", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)
AN5_btn = ctk.CTkButton(master=main_frame, width=300, height=40, state='normal', text="AN5", corner_radius=0, border_color='#00bfc2', border_width=0.5, hover=True,)

'''List of slots'''
A_slot = [A_mon_btn, A_wed_btn, A_thu_btn]
B_slot = [B_mon_btn, B_wed_btn, B_thu_btn]
C_slot = [C_mon_btn, C_wed_btn, C_thu_btn]
D_slot = [D_mon_btn, D_tue_btn, D_fri_btn]
E_slot = [E_tue_btn, E_thu_btn, E_fri_btn]
F_slot = [F_tue_btn, F_wed_btn, F_fri_btn]
G_slot = [G_tue_btn, G_wed_btn, G_fri_btn]
P_slot = [P_mon_btn, P_thu_btn]
Q_slot = [Q_mon_btn, Q_thu_btn]
R_slot = [R_tue_btn, R_fri_btn]
S_slot = [S_tue_btn, S_fri_btn]


# place monday slots on grid
A_mon_btn.grid(column=1, row=1,)
B_mon_btn.grid(column=2, row=1,)
C_mon_btn.grid(column=3, row=1)
D_mon_btn.grid(column=4, row=1, rowspan=2, pady=(0,10))
P_mon_btn.grid(column=6, row=1,)
Q_mon_btn.grid(column=7, row=1,)
FN1_btn.grid(column=1, row=2, columnspan=3, pady=(0,10))
AN1_btn.grid(column=6, row=2, columnspan=2, pady=(0,10))

# place tuesday slots on grid
D_tue_btn.grid(column=1, row=3,)
E_tue_btn.grid(column=2, row=3,)
F_tue_btn.grid(column=3, row=3)
G_tue_btn.grid(column=4, row=3, rowspan=2, pady=(0,10))
R_tue_btn.grid(column=6, row=3,)
S_tue_btn.grid(column=7, row=3,)
FN2_btn.grid(column=1, row=4, columnspan=3, pady=(0,10))
AN2_btn.grid(column=6, row=4, columnspan=2, pady=(0,10))

# place wednesday slots on grid
B_wed_btn.grid(column=1, row=5,)
C_wed_btn.grid(column=2, row=5,)
A_wed_btn.grid(column=3, row=5)
G_wed_btn.grid(column=4, row=5, rowspan=2, pady=(0,10))
F_wed_btn.grid(column=6, row=5,)
FN3_btn.grid(column=1, row=6, columnspan=3, pady=(0,10))
AN3_btn.grid(column=6, row=6, columnspan=2, pady=(0,10))

# place thursday slots on grid
C_thu_btn.grid(column=1, row=7,)
A_thu_btn.grid(column=2, row=7,)
B_thu_btn.grid(column=3, row=7)
E_thu_btn.grid(column=4, row=7, rowspan=2, pady=(0,10))
Q_thu_btn.grid(column=6, row=7,)
P_thu_btn.grid(column=7, row=7,)
FN4_btn.grid(column=1, row=8, columnspan=3, pady=(0,10))
AN4_btn.grid(column=6, row=8, columnspan=2, pady=(0,10))
six_nine_thu_btn.grid(column = 8, row=7, rowspan=2, pady=(0,10))

#place friday slots on grid
E_fri_btn.grid(column=1, row=9,)
F_fri_btn.grid(column=2, row=9,)
D_fri_btn.grid(column=3, row=9)
G_fri_btn.grid(column=4, row=9, rowspan=2, pady=(0,10))
S_fri_btn.grid(column=6, row=9,)
R_fri_btn.grid(column=7, row=9,)
FN5_btn.grid(column=1, row=10, columnspan=3, pady=(0,10))
AN5_btn.grid(column=6, row=10, columnspan=2, pady=(0,10))

#nigga was here

app.mainloop()