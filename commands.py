import customtkinter as ctk
import os

def open_calendar_file():
    pass

def open_source_code():
    pass

def limit_entry_size(limit : int, item : ctk.StringVar, *args):
    print("called limit func")
    # print(args)
    print(item,'bla', limit)
    value = item.get()
    print(value, '\n\n')
    if (len(value) > limit):
        item.set(value[:limit])

def dialog_ok_clicked(placeholders : tuple[ctk.StringVar], master : ctk.CTkToplevel):
    print("called ok")
    pass

def dialog_cancel_clicked():
    print("called cancel")
    pass


def modify_slot(btn : ctk.CTkButton, all_slots):
    """
    Called on Slot/Button Press.
    \nCreates a TopLevel and takes user input for Course Title, Code and Venue. Appropriately changes button label.
    """
    print(btn)
    dialog = ctk.CTkToplevel(fg_color = '#121212')
    dialog.title("Edit Slot Details")
    dialog.resizable(False, False)
    # set transparency to 0 until window is completely rendered
    dialog.attributes("-alpha", 0)
    dialog.update_idletasks()
    # print('\n',btn)
    btn_label_text = str(btn.cget("text"))
    # print(btn_label_text)
    course_title_placeholder = ctk.StringVar(master = dialog, value="Max 12 char")
    course_code_placeholder =  ctk.StringVar(master = dialog, value="Max 6 char")
    course_venue_placeholder = ctk.StringVar(master = dialog, value="Max 6 char")
    course_title_placeholder.trace_add("write", lambda *args, item=course_title_placeholder, n=12 : limit_entry_size(n, item, *args))
    course_code_placeholder.trace_add("write", lambda *args, item=course_code_placeholder, n=6 : limit_entry_size(n, item, *args))
    course_venue_placeholder.trace_add("write", lambda *args, item=course_venue_placeholder, n=6 : limit_entry_size(n, item, *args))
    
    entry_placeholders = (course_title_placeholder, course_code_placeholder, course_venue_placeholder)

    if (len(btn_label_text) == 1 or len(btn_label_text) == 3):
        slot = btn_label_text
    else:
        slot = btn_label_text[-2]

        
    dialog_width=300
    dialog_height=300
    screen_width=2200 
    screen_height=1200
    x_coordinate=int((screen_width/2)-(dialog_width/2))
    y_coordinate = int((screen_height/2) - (dialog_height/2))
    dialog.geometry("{}x{}+{}+{}".format(dialog_width, dialog_height, x_coordinate, y_coordinate))

    header_label = ctk.CTkLabel(master=dialog, width=290, justify="center", text=f'Editing {slot} Slot Details', anchor="center", font=("Helvetica", 20))

    course_title_text = ctk.CTkTextbox(master = dialog, activate_scrollbars=False, state="normal", height=20, fg_color='transparent') 
    course_title_text.insert("0.0", "Course Title *")
    course_title_text.configure(state="disabled")

    course_code_text = ctk.CTkTextbox(master = dialog, activate_scrollbars=False, state="normal", height=20, width=100, fg_color='transparent') 
    course_code_text.insert("0.0", "Course Code *")
    course_code_text.configure(state="disabled")

    course_venue_text = ctk.CTkTextbox(master = dialog, activate_scrollbars=False, state="normal", height=20, width=102, fg_color='transparent') 
    course_venue_text.insert("0.0", "Lecture Venue")
    course_venue_text.configure(state="disabled")

    course_title_entry = ctk.CTkEntry(master = dialog, width=275, textvariable=course_title_placeholder)    
    course_code_entry = ctk.CTkEntry(master = dialog, width=100 , textvariable=course_code_placeholder)
    course_venue_entry = ctk.CTkEntry(master = dialog, width=100, textvariable=course_venue_placeholder)
    
    ok_button = ctk.CTkButton(master=dialog, width=120, text="OK", command = lambda master=dialog, item = entry_placeholders : dialog_ok_clicked(item, master))
    cancel_button = ctk.CTkButton(master=dialog, width=120, text="Cancel", command = dialog_cancel_clicked)

    header_label.grid(row=0, column=0, columnspan=2, sticky='nw', padx=(10,10), pady=(20,0))

    course_title_text.grid(row=1, column=0, columnspan=2, sticky='nw', padx=(9,10), pady=(20,0))
    course_title_entry.grid(row=2, column=0, columnspan=2, sticky='nw', padx=(10,10), pady=(0,10))
    course_code_text.grid(row=3, column=0, sticky='nw', padx=(9,10))
    course_code_entry.grid(row=4, column =0, sticky='nw', padx=(10,10), pady=(0, 40))
    course_venue_text.grid(row=3, column=1, sticky='ne', padx=(10,20))
    course_venue_entry.grid(row=4, column=1, sticky='ne', padx=(10,20), pady=(0, 40))

    ok_button.grid(row=5, column=0, sticky='nw', padx=(10,20))
    cancel_button.grid(row=5, column=1, sticky='ne', padx=(10,20))

    # set transparency to 1
    dialog.attributes("-alpha", 1)
    dialog.attributes("-topmost", True)
    dialog.focus_set()

