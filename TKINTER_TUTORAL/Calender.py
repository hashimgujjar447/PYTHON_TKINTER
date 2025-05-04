from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk


win=Tk()
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)

# calendar=Calendar(win, selectmode='day', year=2023, month=10, day=1)
# calendar.pack(pady=20)

# btn=Button(win, text="Get Date", command=lambda: print(calendar.get_date()))
# btn.pack(pady=40)

# date_entry=DateEntry(win, selectmode="day", year=2023, month=10, day=1)
# date_entry.pack(pady=20)
size_grip=ttk.Sizegrip(win)
size_grip.grid(row=0,sticky=(S, E))

win.mainloop()


