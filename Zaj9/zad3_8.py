import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=30)
root.option_add("*Font", default_font)

liczb = 0
y = 0
tryb =0

ta = tk.Text(root, height=1, width=5)
ta.insert(tk.END, liczb)

def add( y):
	global tryb
	if tryb == 1:
		tryb = 0
	global liczb
	liczb += y	
	ta.config(state=tk.NORMAL)
	ta.delete('1.0', tk.END)
	ta.insert(tk.END,liczb)
	ta.config(state=tk.DISABLED)

def mult( y):
	global tryb
	if tryb == 1:
		tryb = 0
	global liczb
	liczb *= y
	ta.config(state=tk.NORMAL)
	ta.delete('1.0', tk.END)
	ta.insert(tk.END,liczb)
	ta.config(state=tk.DISABLED)

def divide( y):
	global tryb
	if tryb == 1:
		tryb = 0
	global liczb
	try:
		liczb /= y
	except:
		y=1
	ta.config(state=tk.NORMAL)
	ta.delete('1.0', tk.END)
	ta.insert(tk.END,liczb)
	ta.config(state=tk.DISABLED)

def decr( y):
	global tryb
	if tryb == 1:
		tryb = 0
	global liczb
	liczb -= y
	ta.config(state=tk.NORMAL)
	ta.delete('1.0', tk.END)
	ta.insert(tk.END,liczb)
	ta.config(state=tk.DISABLED)

def zmien(uu):
	global tryb
	global y
	if tryb == 0:
		y = uu
	else:
		i=0
		while i < tryb:
			uu=float(float(uu)/10)
			i+=1
		y += uu
		tryb += 1
	ta.config(state=tk.NORMAL)
	ta.delete('1.0', tk.END)
	ta.insert(tk.END,y)
	ta.config(state=tk.DISABLED)

def przyc():
	global tryb
	if tryb == 0:
		tryb = 1
	else:
		tryb = 0

bt_0 = tk.Button(root, text="0", command=lambda: zmien(0))
bt_1 = tk.Button(root, text="1", command=lambda: zmien(1))
bt_2 = tk.Button(root, text="2", command=lambda: zmien(2))
bt_3 = tk.Button(root, text="3", command=lambda: zmien(3))
bt_4 = tk.Button(root, text="4", command=lambda: zmien(4))
bt_5 = tk.Button(root, text="5", command=lambda: zmien(5))
bt_6 = tk.Button(root, text="6", command=lambda: zmien(6))
bt_7 = tk.Button(root, text="7", command=lambda: zmien(7))
bt_8 = tk.Button(root, text="8", command=lambda: zmien(8))
bt_9 = tk.Button(root, text="9", command=lambda: zmien(9))
bt_prz = tk.Button(root, text=",", command=lambda: przyc())
bt = tk.Button(root, text="+", command=lambda: add(y))
bt1 = tk.Button(root, text="-", command=lambda: decr(y))
bt2 = tk.Button(root, text="*", command=lambda: mult(y))
bt3 = tk.Button(root, text="/", command=lambda: divide(y))

ta.grid(column=0, row=0,columnspan=6, sticky = tk.W+tk.E)
bt_0.grid(column=0, row=4,columnspan=2, sticky = tk.W+tk.E)
bt_1.grid(column=0, row=3, sticky = tk.W+tk.E)
bt_2.grid(column=1, row=3, sticky = tk.W+tk.E)
bt_3.grid(column=2, row=3, sticky = tk.W+tk.E)
bt_4.grid(column=0, row=2, sticky = tk.W+tk.E)
bt_5.grid(column=1, row=2, sticky = tk.W+tk.E)
bt_6.grid(column=2, row=2, sticky = tk.W+tk.E)
bt_7.grid(column=0, row=1, sticky = tk.W+tk.E)
bt_8.grid(column=1, row=1, sticky = tk.W+tk.E)
bt_9.grid(column=2, row=1, sticky = tk.W+tk.E)
bt.grid(column=3, row=1, sticky = tk.W+tk.E)
bt1.grid(column=3, row=2, sticky = tk.W+tk.E)
bt2.grid(column=3, row=3, sticky = tk.W+tk.E)
bt3.grid(column=3, row=4,sticky = tk.W+tk.E)
bt_prz.grid(column=2, row=4, sticky = tk.W+tk.E)
ta.config(state=tk.DISABLED)

root.mainloop()