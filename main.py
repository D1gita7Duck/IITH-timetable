import widgets

widgets.commands.db.initialize_db()
widgets.commands.db.create_slots_text_table()

app = widgets.App()
app.mainloop()