import customtkinter as ctk
from PIL import Image
import CTkMessagebox
from CTkDateEntry.dateentry import DateTextEntry

course_add_img = ctk.CTkImage(Image.open("icons\\course_add.png"), size = (40,40))
course_delete_img = ctk.CTkImage(Image.open("icons\\course_delete.png"), size = (40,40))

def show_warning(msg : str):
    warning_window = CTkMessagebox.CTkMessagebox(
                        title="Warning!",
                        message=msg,
                        icon="warning",
                        option_1="Retry",
                        sound=True,
                        cancel_button='cross',
                    )


class CourseEntry(ctk.CTkFrame):
    def __init__(self,
                 master,
                 
                 title_text : str = "Insert Title",
                 title_justify: str = "center",
                 combobox_command = None,
                 combobox_values : list[str] = ["Enter a Value"],
                 add_btn_cmd = None,
                 delete_btn_cmd = None,
                 clear_entries = None,
                 push_entries = None,

                 width = 200, 
                 height = 400, 
                 corner_radius = None, 
                 border_width = None, 
                 bg_color = "transparent", 
                 fg_color = None,
                 border_color = None, 
                 background_corner_colors = None, 
                 overwrite_preferred_drawing_method = None,

                 **kwargs
                 ):
        """
        Passing combobox_cmd overrides on_combobox_click functionalities
        """
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._title_text = title_text
        self._title_justify = title_justify
        self._combobox_values = combobox_values
        self._combobox_command = combobox_command
        self._add_btn_cmd = add_btn_cmd
        self._delete_btn_cmd = delete_btn_cmd
        self._clear_entries = clear_entries
        self._push_entries = push_entries
        self._values_entries_dict = {}
        self._varnum = 0
        self._entry_var = "Enter a Value"
        
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12), minsize=50)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8,), minsize=50)

        self.title_label = ctk.CTkLabel(master=self, height=40 ,text=self._title_text, justify = self._title_justify, anchor = "center", font=("Helvetica", 25))
        self.title_label.grid(row=0, column = 0, columnspan = 9, padx=(10,10),pady=(20,20), sticky='nsew')

        self.combovar = ctk.StringVar(value = "Enter a Value")
        self.combobox = ctk.CTkComboBox(master = self, width=250, height=45, values=self._combobox_values, variable=self.combovar, state="readonly", command=self.on_combobox_click)
        self.combobox.grid(row = 1, column = 0, columnspan = 4, padx=(20,10), pady=(20,10), sticky='nsew')

        self.add_btn = ctk.CTkButton(master = self, width = 0, height = 0, image=course_add_img, fg_color="transparent", border_width=0, text = "", corner_radius=100, hover=False, command=self.on_add_click)
        self.add_btn.grid(row = 1, column = 5, padx=(10,10), pady=(20,10), sticky='nsew')

        self.delete_btn = ctk.CTkButton(master = self, width = 0, height = 0, image=course_delete_img, fg_color="transparent", border_width=0, text = "", corner_radius=100, hover=False, command = self.on_delete_click)
        self.delete_btn.grid(row = 1, column = 7, padx=(10,10), pady=(20,10), sticky='nsew')

        self.entries_frame = ctk.CTkFrame(master = self, width = 150, height = 300,)
        self.entries_frame.grid(row = 3, column = 0, columnspan = 11, rowspan = 9, sticky = 'nsew', padx=(10,10), pady=(0,20))
        
        # entrybox text variables
        self.entries_frame.course_title_placeholder = ctk.StringVar(master = self, value="Course Title")
        self.entries_frame.course_code_placeholder =  ctk.StringVar(master = self, value="Max 6 char")
        self.entries_frame.course_venue_placeholder = ctk.StringVar(master = self, value="Max 6 char")
        self.entries_frame.course_start_segment_placeholder = ctk.StringVar(master = self, value="Max 1 char")
        self.entries_frame.course_end_segment_placeholder = ctk.StringVar(master = self, value="Max 1 char")
        self.entries_frame.slot_text_placeholder = ctk.StringVar(master = self, value = "Max 12 char")
        self.entries_frame.slot_placeholder = ctk.StringVar(master = self, value = "Max 3 char")

        self._placeholders = (self.entries_frame.course_title_placeholder,
                              self.entries_frame.course_code_placeholder,
                              self.entries_frame.course_venue_placeholder,
                              self.entries_frame.course_start_segment_placeholder,
                              self.entries_frame.course_end_segment_placeholder,
                              self.entries_frame.slot_text_placeholder,
                              self.entries_frame.slot_placeholder,
                              )

        self.entries_frame.course_code_placeholder.trace_add("write", lambda *args, item= self.entries_frame.course_code_placeholder, n=6 : self.limit_entry_size(n, item, *args))
        self.entries_frame.course_venue_placeholder.trace_add("write", lambda *args, item=self.entries_frame.course_venue_placeholder, n=6 : self.limit_entry_size(n, item, *args))
        self.entries_frame.slot_text_placeholder.trace_add("write", lambda *args, item=self.entries_frame.slot_text_placeholder, n=12 : self.limit_entry_size(n, item, *args))
        self.entries_frame.slot_placeholder.trace_add("write", lambda *args, item=self.entries_frame.slot_placeholder, n=3 : self.limit_entry_size(n, item, *args))
        self.entries_frame.course_start_segment_placeholder.trace_add("write", lambda *args, item=self.entries_frame.course_start_segment_placeholder, n=1 : self.limit_entry_size(n, item, *args))
        self.entries_frame.course_end_segment_placeholder.trace_add("write", lambda *args, item=self.entries_frame.course_end_segment_placeholder, n=1 : self.limit_entry_size(n, item, *args))

        self.entries_frame.course_title_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, fg_color='transparent') 
        self.entries_frame.course_title_textbox.insert("0.0", "Course Title *")
        self.entries_frame.course_title_textbox.configure(state="disabled")

        self.entries_frame.course_code_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent') 
        self.entries_frame.course_code_textbox.insert("0.0", "Course Code *")
        self.entries_frame.course_code_textbox.configure(state="disabled")

        self.entries_frame.course_venue_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent') 
        self.entries_frame.course_venue_textbox.insert("0.0", "Lecture Venue")
        self.entries_frame.course_venue_textbox.configure(state="disabled")
        
        self.entries_frame.slot_text_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent')
        self.entries_frame.slot_text_textbox.insert("0.0", "Slot Text *")
        self.entries_frame.slot_text_textbox.configure(state="disabled")

        self.entries_frame.slot_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent')
        self.entries_frame.slot_textbox.insert("0.0", "Slot *")
        self.entries_frame.slot_textbox.configure(state="disabled")

        self.entries_frame.start_segment_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent')
        self.entries_frame.start_segment_textbox.insert("0.0", "Start Segment *")
        self.entries_frame.start_segment_textbox.configure(state="disabled")
        
        self.entries_frame.end_segment_textbox = ctk.CTkTextbox(master = self.entries_frame, activate_scrollbars=False, state="normal", height=20, width=101, fg_color='transparent')
        self.entries_frame.end_segment_textbox.insert("0.0", "End Segment *")
        self.entries_frame.end_segment_textbox.configure(state="disabled")

        self.entries_frame.course_title_entry = ctk.CTkEntry(master = self.entries_frame, width=225, textvariable=self.entries_frame.course_title_placeholder)    
        self.entries_frame.course_code_entry = ctk.CTkEntry(master =  self.entries_frame, width=100 , textvariable=self.entries_frame.course_code_placeholder)
        self.entries_frame.course_venue_entry = ctk.CTkEntry(master = self.entries_frame, width=100, textvariable=self.entries_frame.course_venue_placeholder)
        self.entries_frame.slot_text_entry = ctk.CTkEntry(master = self.entries_frame, width=100, textvariable=self.entries_frame.slot_text_placeholder)
        self.entries_frame.slot_entry = ctk.CTkEntry(master = self.entries_frame, width=100, textvariable=self.entries_frame.slot_placeholder)
        self.entries_frame.start_segment_entry = ctk.CTkEntry(master = self.entries_frame, width=100, textvariable=self.entries_frame.course_start_segment_placeholder)
        self.entries_frame.end_segment_entry = ctk.CTkEntry(master = self.entries_frame, width=100, textvariable=self.entries_frame.course_end_segment_placeholder)

        self.entries_frame.course_title_textbox.grid(row=1, column=0, columnspan=2, sticky='nw', padx=(10,10), pady=(20,0))
        self.entries_frame.slot_text_textbox.grid(row = 1, column=6, sticky='nw', padx=(10,10), pady=(20,0))
        self.entries_frame.slot_textbox.grid(row = 1, column=7, sticky='nw', padx=(10,10), pady=(20,0))
        self.entries_frame.course_title_entry.grid(row=2, column=0, columnspan=2, sticky='nw', padx=(10,10), pady=(0,20))
        self.entries_frame.slot_text_entry.grid(row=2, column=6, sticky='nw', padx=(10,10), pady=(0,20))
        self.entries_frame.slot_entry.grid(row=2, column =7, sticky='nw', padx=(10,10), pady=(0,20))
        self.entries_frame.course_code_textbox.grid(row=3, column=0, sticky='nw', padx=(10,10))
        self.entries_frame.course_venue_textbox.grid(row=3, column=1, sticky='ne', padx=(10,20))
        self.entries_frame.start_segment_textbox.grid(row=3, column=6, sticky='nw', padx=(10,10))
        self.entries_frame.end_segment_textbox.grid(row=3, column=7, sticky='nw', padx=(10,10))
        self.entries_frame.course_code_entry.grid(row=4, column =0, sticky='nw', padx=(10,10), pady=(0, 40))
        self.entries_frame.course_venue_entry.grid(row=4, column=1, sticky='ne', padx=(10,20), pady=(0, 40))
        self.entries_frame.start_segment_entry.grid(row=4, column =6, sticky='nw', padx=(10,10), pady=(0, 40))
        self.entries_frame.end_segment_entry.grid(row=4, column =7, sticky='nw', padx=(10,10), pady=(0, 40))

        self.entries_frame.clear_btn = ctk.CTkButton(master=self.entries_frame, width = 225, height=40, text="Clear", anchor="center", command=self.clear_entries)
        self.entries_frame.clear_btn.grid(row = 13, column = 0, columnspan =2, sticky='nw', padx=(10,20), pady=(0,10))

        self.entries_frame.push_btn = ctk.CTkButton(master=self.entries_frame, width = 225, height=40, text="Push", anchor="center", command=self.commit_entries)
        self.entries_frame.push_btn.grid(row = 13, column = 6, columnspan =2, sticky='nw', padx=(10,10), pady=(0,10))

        self.close_self_btn = ctk.CTkButton(master = self, width=100, height=40, text="Close", anchor="center", command = self.master.destroy)
        self.close_self_btn.grid(row=12, column = 0, columnspan = 9, padx=(50,50),pady=(10,20), sticky='nsew')

    def limit_entry_size(self, limit : int, item : ctk.StringVar, *args):
        # print("called limit func")
        # print(args)
        # print(item,'bla', limit)
        value = item.get()
        print(value, '\n\n')
        if (len(value) > limit):
            item.set(value[:limit])
    
    def check_entries(self):
        for i in range(7):
            input_text = self._placeholders[i].get()
            match i:
                case 0:
                    if input_text == "Course Title":
                        show_warning("Enter Course Title")
                        return 1
                case 1:
                    if input_text == "Max 6 char":
                        show_warning("Enter Course Code")
                        return 1
                case 2:
                    continue
                case 3:
                    if input_text == "Max 1 char":
                        show_warning("Enter Start Segment")
                        return 1
                case 4:
                    if input_text == "Max 1 char":
                        show_warning("Enter End Segment")
                        return 1
                case 5:
                    if input_text == "Max 12 char":
                        show_warning("Enter Slot Text")
                        return 1
                case 6:
                    if input_text == "Max 3 char":
                        show_warning("Enter Course Slot")
                        return 1
                case _:
                    return 0

    def set_entries_to(self, box_value):
        """
        Relies on variables of the CourseEntry Object, not on backend variables. Unwanted behaviour.\n
        USE set_entries_to_given_values instead.
        """
        self.combobox.set(box_value)
        print(f'$${self._values_entries_dict}$$')
        for i in range(7):
            self._placeholders[i].set(self._values_entries_dict[box_value][i])
        self._entry_var = box_value

    def set_entries_to_given_values(self, box_value, values):
        """
        values is tuple of values in correct order for respective placeholders
        """
        self.combobox.set(box_value)
        for i in range(7):
            self._placeholders[i].set(values[i])

    def reset_combobox(self):
        self._combobox_values = ["Enter a Value"]
        self.combobox.configure(values = self._combobox_values)
        self._values_entries_dict.clear()
        self.combobox.set("Enter a Value")
        self._entry_var = "Enter a Value"
        
        self.clear_entries()

    def on_combobox_click(self, box_value):
        print(box_value)
        if self._combobox_command is not None:
            self._combobox_command(box_value)
            return
        
        if self.check_entries():
            self.combobox.set(self._entry_var)
            return
        if (box_value == "Enter a Value"):
            return

        self.set_entries_to(box_value)
        
    def on_add_click(self):
        if self.check_entries():
            return
        new_option = "New Course " + str(self._varnum)
        self._varnum += 1
        self._combobox_values.append(new_option)
        self.combobox.configure(values = self._combobox_values)
        self.combobox.set(new_option)
        self._entry_var = new_option

        self.clear_entries()

        if self._add_btn_cmd is not None:
            self._add_btn_cmd()

    def on_delete_click(self):
        print(f'\nCourseEntry Object DELETE CALLED\n')
        box_value = self.combobox.get()

        if self._delete_btn_cmd is not None:
            self._delete_btn_cmd(self._placeholders)
            
        if len(self._combobox_values) == 1:
            self.reset_combobox()
        else:
            index = self._combobox_values.index(box_value) - 1
            self.combobox.set(self._combobox_values[index])
            self._entry_var = self._combobox_values[index]
            # self.set_entries_to(self._combobox_values[index])
            self._combobox_command(self._combobox_values[index])
            self._combobox_values.remove(box_value)
            self.combobox.configure(values = self._combobox_values)
            print(self._values_entries_dict.pop(box_value, "Trying to delete new course"))
            
    def clear_entries(self):
        self.entries_frame.course_title_placeholder.set("Course Title")
        self.entries_frame.course_code_placeholder.set("Max 6 char")
        self.entries_frame.course_venue_placeholder.set("Max 6 char")
        self.entries_frame.course_start_segment_placeholder.set("Max 1 char")
        self.entries_frame.course_end_segment_placeholder.set("Max 1 char")
        self.entries_frame.slot_text_placeholder.set("Max 12 char")
        self.entries_frame.slot_placeholder.set("Max 3 char")

        if self._clear_entries is not None:
            self._clear_entries(self._placeholders)
    
    def commit_entries(self):
        if self.check_entries():
            return
        
        key = self.entries_frame.course_title_placeholder.get()
        value = [var.get() for var in self._placeholders]
        box_value = self.combobox.get()

        if "Enter a Value" in self._combobox_values:
            self._combobox_values.remove("Enter a Value")
        
        if "New Course" in box_value:
            self._combobox_values.remove(box_value)

        if key not in self._combobox_values:
            self._combobox_values.append(key)
        
        self.combobox.configure(values = self._combobox_values)
        self.combobox.set(key)
        self._values_entries_dict.update({key : value})
        # print(self._values_entries_dict)

        if self._push_entries is not None:
            self._push_entries(key, value)



class SegmentEntry(ctk.CTkFrame):
    def __init__(self,
                 master,
                 width = 200,
                 height = 200,
                 corner_radius = None,
                 border_width = None,
                 bg_color = "transparent",
                 fg_color = None,
                 border_color = None,
                 background_corner_colors = None,
                 overwrite_preferred_drawing_method = None,

                 option_menu_cmd = None,

                 title_text = "Editing Segments",
                 title_justify = "center",
                 
                 date_format = 0,
                 delimiter = '/',
                 invalid_date_cmd = show_warning,
                 
                 clear_entries = None,
                 push_entries = None,

                 **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.grid_columnconfigure((0,1,2,3,4,5,6,), minsize=50)

        self._option_menu_cmd = option_menu_cmd
        self._title_text = title_text
        self._title_justify = title_justify
        self._segment_values = ['1', '2', '3', '4', '5', '6']
        self._date_format = date_format
        self._delimiter = delimiter
        self._invalid_date_cmd = invalid_date_cmd
        self._clear_entries = clear_entries
        self._push_entries = push_entries

        self.title_label = ctk.CTkLabel(master=self, height=40 ,text=self._title_text, justify = self._title_justify, anchor = "center", font=("Helvetica", 25))
        self.title_label.grid(row=0, column = 0, columnspan = 9, padx=(10,10),pady=(20,10), sticky='nsew')

        self.segment_label = ctk.CTkLabel(master=self, text="Segment  :", font=("Helvetica", 18))
        self.segment_label.grid(row=1, column=2, columnspan=2, padx=(10,0), pady=(10,10))
        self.option_menu = ctk.CTkOptionMenu(master = self, width = 75, values=self._segment_values, command=self._option_menu_cmd)
        self.option_menu.grid(row=1, column=4, padx=(10,10), pady=(10,10))

        self.start_date_label = ctk.CTkLabel(master=self, text="Start Date")
        self.end_date_label = ctk.CTkLabel(master=self, text="End Date")
        self.start_date_label.grid(row=2, column=1, padx=(10,10), pady=(0,10))
        self.end_date_label.grid(row=2, column=5, padx=(10,10), pady=(0,10))

        self.start_dateentry = DateTextEntry(master=self, date_format=self._date_format, width=100, delimiter=self._delimiter, invalid_date_cmd=self._invalid_date_cmd)
        self.end_dateentry =   DateTextEntry(master=self, date_format=self._date_format, width=100, delimiter=self._delimiter, invalid_date_cmd=self._invalid_date_cmd)
        self.start_dateentry.grid(row=3, column=1, padx=(10,10), pady=(0,20))
        self.end_dateentry.grid(row=3, column=5, padx=(10,10), pady=(0,20))

        self.clear_btn = ctk.CTkButton(master=self, width = 200, height=40, text="Clear", anchor="center", command=self.clear_entries)
        self.clear_btn.grid(row=4, column = 0, columnspan =4, sticky='nw', padx=(10,20), pady=(0,10))

        self.push_btn = ctk.CTkButton(master=self, width = 200, height=40, text="Push", anchor="center", command=self.commit_entries)
        self.push_btn.grid(row=4, column = 4, columnspan =4, sticky='nw', padx=(40,10), pady=(0,10))

        self.close_self_btn = ctk.CTkButton(master = self, width=200, height=40, text="Close", anchor="center", command = self.master.destroy)
        self.close_self_btn.grid(row=5, column = 0, columnspan = 7, padx=(10,10),pady=(10,20), sticky='nsew')
    
        self.date_entries = (self.start_dateentry, self.end_dateentry)
    
    def clear_entries(self):
        self.start_dateentry.reset()
        self.end_dateentry.reset()
        self.option_menu.set('1')

        if self._clear_entries is not None:
            self._clear_entries()

    def commit_entries(self):
        if self._push_entries is not None:
            try:
                self._push_entries(self.option_menu.get(), self.start_dateentry.get_str(), self.end_dateentry.get_str())
            except ValueError as msg:
                show_warning(msg)
        

class HoldidayEntry(ctk.CTkFrame):
    def __init__(self,
                 master,
                 width = 200,
                 height = 200,
                 corner_radius = None,
                 border_width = None,
                 bg_color = "transparent",
                 fg_color = None,
                 border_color = None,
                 background_corner_colors = None,
                 overwrite_preferred_drawing_method = None,

                 option_menu_cmd = None,
                 option_menu_values : list = ["Enter a Value"],

                 title_text = "Editing Holidays",
                 title_justify = "center",
                 
                 date_format = 0,
                 delimiter = '/',
                 invalid_date_cmd = show_warning,
                 
                 clear_entries = None,
                 push_entries = None,
                 add_btn_cmd = None,
                 delete_btn_cmd = None,
                 **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.grid_columnconfigure((0,1,2,3,4,5), minsize=50)

        self._title_text = title_text
        self._title_justify = title_justify
        self._option_menu_cmd = option_menu_cmd
        self._date_format = date_format
        self._delimiter = delimiter
        self._invalid_date_cmd = invalid_date_cmd
        self._clear_entries = clear_entries
        self._push_entries = push_entries
        self._add_btn_cmd = add_btn_cmd
        self._delete_btn_cmd = delete_btn_cmd
        self._option_menu_values = option_menu_values
        self.hol_name_var = ctk.StringVar(value="Holiday")
        self._values_entries_dict = {}
        self._varnum = 0
        self._entry_var = "Enter a Value"

        self.title_label = ctk.CTkLabel(master=self, height=40 ,text=self._title_text, justify = self._title_justify, anchor = "center", font=("Helvetica", 25))
        self.title_label.grid(row=0, column = 0, columnspan = 6, padx=(10,10),pady=(20,10), sticky='nsew')

        self.option_menu = ctk.CTkOptionMenu(master = self, width = 75, height=40, values=self._option_menu_values, command=self.on_option_menu_click)
        self.option_menu.grid(row=1, column=0, padx=(30,10), pady=(10,10))

        self.add_btn = ctk.CTkButton(master = self, width = 0, height = 0, image=course_add_img, fg_color="transparent", text = "", corner_radius=100, hover=False, command=self.on_add_click)
        self.add_btn.grid(row = 1, column = 2, padx=(0,10), pady=(10,10), sticky='nsew')

        self.delete_btn = ctk.CTkButton(master = self, width = 0, height = 0, image=course_delete_img, fg_color="transparent", text = "", corner_radius=100, hover=False, command = self.on_delete_click)
        self.delete_btn.grid(row = 1, column = 3, padx=(0,20), pady=(10,10), sticky='nsew')

        self.hol_name_label = ctk.CTkLabel(master=self, text="Holiday Name")
        self.date_label = ctk.CTkLabel(master=self, text="End Date")
        self.hol_name_label.grid(row=2, column=0, padx=(10,10), pady=(10,10))
        self.date_label.grid(row=2, column=4, padx=(10,10), pady=(10,10))

        self.hol_name_entry = ctk.CTkEntry(master=self, width=100, height=40, textvariable=self.hol_name_var)
        self.date_entry =  DateTextEntry(master=self, date_format=self._date_format, width=100, delimiter=self._delimiter, invalid_date_cmd=self._invalid_date_cmd)
        self.hol_name_entry.grid(row=3, column=0, padx=(10,10), pady=(0,20))
        self.date_entry.grid(row=3, column=4, padx=(10,10), pady=(0,20))

        self.clear_btn = ctk.CTkButton(master=self, width = 100, height=40, text="Clear", anchor="center", command=self.clear_entries)
        self.clear_btn.grid(row = 4, column = 0,  sticky='nw', padx=(30,20), pady=(0,10))

        self.push_btn = ctk.CTkButton(master=self, width = 100, height=40, text="Push", anchor="center", command=self.commit_entries)
        self.push_btn.grid(row = 4, column = 4,  sticky='nw', padx=(10,10), pady=(0,10))

        self.close_self_btn = ctk.CTkButton(master = self, width=100, height=40, text="Close", anchor="center", command = self.master.destroy)
        self.close_self_btn.grid(row=5, column = 0, columnspan = 6, padx=(30,40),pady=(10,20), sticky='nsew')

        self.entries = (self.hol_name_entry, self.date_entry)

    def check_entries(self):
        """
        Returns 1 for any error. Returns 0 if all ok
        """
        if self.hol_name_var == '':
            show_warning("Give Holiday name")
            return 1
        try:
            d = self.date_entry.get_str()
        except ValueError as msg:
            show_warning(msg)
            return 1
        return 0

    def set_entries_to(self, box_value):
        self.option_menu.set(box_value)
        for i in range(2):
            if i == 0:
                self.hol_name_var.set(box_value)
            else:
                self.date_entry.write(self._values_entries_dict[box_value])
        self._entry_var = box_value

    def set_entries_to_given_values(self, box_value, values):
        self.option_menu.set(box_value)
        self.hol_name_var.set(values[0])
        self.date_entry.write(values[1])

    def reset_option_menu(self):
        self._option_menu_values = ["Enter a Value"]
        self.option_menu.configure(values = self._option_menu_values)
        self._values_entries_dict.clear()
        self.option_menu.set("Enter a Value")
        self._entry_var = "Enter a Value"
        
        self.clear_entries()

    def on_option_menu_click(self, box_value):
        if self._option_menu_cmd is not None:
            self._option_menu_cmd(box_value)
            return
        if self.check_entries():
            self.option_menu.set(self._entry_var)
            return
        if (box_value == "Enter a Value"):
            return

        self.set_entries_to(box_value)

    def on_add_click(self):
        if self.check_entries():
            return
        
        new_option = "New Hol " + str(self._varnum)
        self._varnum += 1
        self._option_menu_values.append(new_option)
        self.option_menu.configure(values = self._option_menu_values)
        self.option_menu.set(new_option)
        self._entry_var = new_option

        self.clear_entries()

        if self._add_btn_cmd is not None:
            self._add_btn_cmd()

    def on_delete_click(self):
        box_value = self.option_menu.get()

        if self._delete_btn_cmd is not None:
            self._delete_btn_cmd(self.entries)  
        
        if len(self._option_menu_values) == 1:
            self.reset_option_menu()
        else:
            index = self._option_menu_values.index(box_value) - 1
            self.option_menu.set(self._option_menu_values[index])
            self._entry_var = self._option_menu_values[index]
            self.set_entries_to(self._option_menu_values[index])
            self._option_menu_values.remove(box_value)
            self.option_menu.configure(values = self._option_menu_values)
            print(self._values_entries_dict.pop(box_value, "Trying to delete holiday"))            

    def clear_entries(self):
        self.hol_name_var.set("Holiday")
        self.date_entry.reset()

        if self._clear_entries is not None:
            self._clear_entries(self.entries)
    
    def commit_entries(self):
        if self.check_entries():
            return
        
        key = self.hol_name_var.get()
        value = self.date_entry.get_str()
        box_value = self.option_menu.get()

        if "Enter a Value" in self._option_menu_values:
            self._option_menu_values.remove("Enter a Value")
        if "New Hol" in box_value:
            self._option_menu_values.remove(box_value)
        if key not in self._option_menu_values:
            self._option_menu_values.append(key)
        
        self.option_menu.configure(values = self._option_menu_values)
        self.option_menu.set(key)
        self._values_entries_dict.update({key : value})
        print(self._values_entries_dict)
        
        if self._push_entries is not None:
            self._push_entries(self.hol_name_var.get(), self.date_entry.get_str())