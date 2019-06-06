from tkinter import *
from Pages import *


def open_info(self):
    self.new_window = Toplevel(self.master)
    self.app = Info(self.new_window)

def open_start(self):
    self.new_window2 = Toplevel(self.master)
    self.app2 = CAI(self.new_window2)

def open_help(self):
    self.new_window = Toplevel(self.master)
    self.app = Help(self.new_window)


def open():
    open_info(root)
def startt():
    open_start(root)
def shelp():
    open_help(root)


#Creates main page user interface
root = Tk()
root.geometry("500x200")
root.title("Computer Aided Instruction")
root.resizable(height=FALSE, width=FALSE)

icon = PhotoImage(file = "help.png")
info = PhotoImage(file="info.png")
close = PhotoImage(file="exit.png")
start = PhotoImage(file="start.png")

label_welcome = Label(root, text="Welcome to Math World", font=("Helvetica", 20), fg="red")
label_welcome.place(relx=0.5, y=35, anchor=CENTER )

btn_start = Button(root, text="Quiz", image=start, compound="left", command=startt)
btn_start.place(height=50, x=200, y=100)

btn_help = Button(root, text="Help", image=icon, command=shelp)
btn_help.place(height=55,width=55, x=440, y=145)

btn_info = Button(root, text="Info", image=info, command=open)
btn_info.place(height=55,width=55, x=385, y=145)

btn_exit = Button(root, text="Quit", command=root.destroy, image=close)
btn_exit.place(height=50, width=50, y=150)

root.mainloop()
