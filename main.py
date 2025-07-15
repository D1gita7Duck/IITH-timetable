import widgets

widgets.commands.db.initialize_db()
widgets.commands.db.create_segments_table()
widgets.commands.db.create_courses_table()
widgets.commands.db.create_holidays_table()
widgets.commands.db.create_attendance_table()
widgets.commands.db.create_theme_table()

app = widgets.App()
app.iconbitmap(widgets.resource_path("icons/app_icon.ico"))
app.mainloop()