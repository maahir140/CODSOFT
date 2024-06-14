from tkinter import *
from tkinter import ttk

co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title("")
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

fram_up = Frame(window, width=500, height=50, bg=co2)
fram_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)

#frame_up
app_name = Label(fram_up, text="ContactBook", height=1, font=("Verdana 17 bold"), bg= co2, fg=co0)
app_name.place(x=5, y=5)

#frame_down
l_name = Label(frame_down, text="Name", width= 20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=5, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=70, y=20)

l_name = Label(frame_down, text="Phone", width= 20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=5, y=50)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=70, y=50)

l_name = Label(frame_down, text="Email", width= 20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=5, y=80)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=70, y=80)

l_name = Label(frame_down, text="Gender", width= 20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=5, y=110)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=70, y=110)



window.mainloop()
