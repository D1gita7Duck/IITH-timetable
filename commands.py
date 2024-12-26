import customtkinter as ctk
import CTkMessagebox
import os
import db
import myentry

def show_warning(msg : str):
    warning_window = CTkMessagebox.CTkMessagebox(
                        title="Warning!",
                        message=msg,
                        icon="warning",
                        option_1="Retry",
                        sound=True,
                        cancel_button='cross',
                    )

def modify_button_text_from_db(all_slots : tuple[tuple[ctk.CTkButton]]):
    slot_text = db.get_slot_text()
    for i in range(11):
        for j in range(len(all_slots[i])):
            all_slots[i][j].configure(text = slot_text[i][1])
    
    FN_btns = all_slots[11]
    for i in range(len(FN_btns)):
        FN_btns[i].configure(text = slot_text[11+i][1])

    AN_btns = all_slots[12]
    for i in range(len(AN_btns)):
        AN_btns[i].configure(text = slot_text[16+i][1])

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

def dialog_ok_clicked(placeholders : tuple[ctk.StringVar], master : ctk.CTkToplevel, slot : str, buttons : tuple[ctk.CTkButton]):
    print("called ok")
    initial_text = buttons[0].cget("text")
    output_text=""
    for i in range(3):
        input_text = placeholders[i].get()
        match i:
            case 0:
                if (input_text == "Max 12 char"):
                    show_warning("Please Enter Course Details Properly")
                    output_text=initial_text
                    break
                else:
                    flag0 = 1
                    output_text += input_text
                    output_text += '\n'
            case 1: 
                if (input_text == "Max 6 char"):
                    show_warning("Please Enter Course Details Properly")
                    output_text=initial_text
                    break
                else:
                    flag1 = 1
            case 2:
                if (input_text == "Max 6 char"):
                    show_warning("Please Enter Course Details Properly")
                    output_text=initial_text
                    break
                else:
                    flag2 = 1
                    output_text += input_text
                    output_text += f'\t({slot})'
                    if (flag0 and flag1 and flag2):
                        master.destroy()
    print(output_text)
    db.write_button_text(slot, output_text)
    for btn in buttons:
        btn.configure(text=output_text)

def dialog_cancel_clicked(master : ctk.CTkToplevel):
    print("called cancel")
    master.destroy()


def modify_slot(btn : ctk.CTkButton, all_btns_in_slot):
    """
    Called on Slot/Button Press.
    \nCreates a TopLevel and takes user input for Course Title, Code and Venue. Appropriately changes button label.
    """
    # print(btn)
    if (len(all_btns_in_slot) == 5):
        all_btns_in_slot = btn,  # weird bug fix
    # print(all_btns_in_slot)

    dialog = ctk.CTkToplevel(fg_color = '#121212')
    dialog.title("Edit Slot Details")
    dialog.resizable(False, False)

    # set transparency to 0 until window is completely rendered
    dialog.attributes("-alpha", 0)
    dialog.update_idletasks()

    btn_label_text = str(btn.cget("text"))
    # print(btn_label_text)
    course_title_placeholder = ctk.StringVar(master = dialog, value="Max 12 char")
    course_code_placeholder =  ctk.StringVar(master = dialog, value="Max 6 char")
    course_venue_placeholder = ctk.StringVar(master = dialog, value="Max 6 char")
    course_title_placeholder.trace_add("write", lambda *args, item=course_title_placeholder, n=12 : limit_entry_size(n, item, *args))
    course_code_placeholder.trace_add("write", lambda *args, item=course_code_placeholder, n=6 : limit_entry_size(n, item, *args))
    course_venue_placeholder.trace_add("write", lambda *args, item=course_venue_placeholder, n=6 : limit_entry_size(n, item, *args))
    
    entry_placeholders = (course_title_placeholder, course_code_placeholder, course_venue_placeholder)

    if (len(btn_label_text) == 1 or len(btn_label_text) == 3 or btn_label_text == "AN3/US"):
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
    
    ok_button = ctk.CTkButton(master=dialog, width=120, text="OK", command = lambda item = entry_placeholders, master=dialog, s=slot, btns=all_btns_in_slot: dialog_ok_clicked(item, master, s, btns))
    cancel_button = ctk.CTkButton(master=dialog, width=120, text="Cancel", command = lambda master=dialog: dialog_cancel_clicked(master))

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

def edit_courses():
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

    entry_frame = myentry.CourseEntry(master = edit_course_win, title_text="Editing Courses")
    entry_frame.pack(padx=(10,10), pady=(20,10))

    # set transparency to 1
    edit_course_win.attributes("-alpha", 1)
    edit_course_win.attributes("-topmost", True)
    edit_course_win.focus_set()
    

def edit_segments():
    edit_segment_win = ctk.CTkToplevel(fg_color = '#121212')
    
    edit_segment_win.title("Edit Segment Details")
    edit_segment_win.resizable(False, False)
    # set transparency to 0 until window is completely rendered
    edit_segment_win.attributes("-alpha", 0)
    edit_segment_win.update_idletasks()

    edit_segment_win_width=700
    edit_segment_win_height=500
    screen_width=2200
    screen_height=1200
    x_coordinate=int((screen_width/2)-(edit_segment_win_width/2))
    y_coordinate = int((screen_height/2) - (edit_segment_win_height/2))
    edit_segment_win.geometry("{}x{}+{}+{}".format(edit_segment_win_width, edit_segment_win_height, x_coordinate, y_coordinate))

    entry_frame = myentry.SegmentEntry(master=edit_segment_win)
    entry_frame.pack(padx=(10,10), pady=(20,10))

    # set transparency to 1
    edit_segment_win.attributes("-alpha", 1)
    edit_segment_win.attributes("-topmost", True)
    edit_segment_win.focus_set()