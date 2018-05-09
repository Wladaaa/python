import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=30)
root.option_add("*Font", default_font)

bt = tk.Button(root, text="BUTTON")
ta = tk.Text(root, height=1, width=5,state="disabled")
ta.grid(column=0, row=0,columnspan=3)
bt.grid(column=0, row=1,columnspan=2)

root.mainloop()