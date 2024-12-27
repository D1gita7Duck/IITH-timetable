import widgets

widgets.commands.db.initialize_db()
widgets.commands.db.create_segments_table()
widgets.commands.db.create_courses_table()

app = widgets.App()
app.mainloop()