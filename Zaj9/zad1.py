import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=30)
root.option_add("*Font", default_font)

def massB():
	tkMB.showinfo("Message","Massss")

bt = tk.Button(root, text="BUTTON",command=massB)

def ReadV(a):
	print (a.get())
 	if(a.get()==1):
 		bt.configure(fg="red")
 	elif(a.get()==2):
 		bt.configure(fg="green")
 	else:
 		bt.configure(fg="blue")


v = tk.IntVar()

rb1 = tk.Radiobutton(root, text="R", variable = v, value = 1, command=lambda:ReadV(v))
rb1.grid(column=0, row=0)
rb2 = tk.Radiobutton(root, text="G", variable = v, value = 2, command=lambda:ReadV(v))
rb2.grid(column=1, row=0)
rb3 = tk.Radiobutton(root, text="B", variable = v, value = 3, command=lambda:ReadV(v))
rb3.grid(column=2, row=0)

bt.grid(row = 3, column = 0,columnspan=3)

root.mainloop()