import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB

root = tk.Tk()

# def labelConf(label, txt):
# 	label.config(text = txt, fg = "light green", bg = "dark green")

# label= tk.Label(root, text = "Hello world!")

# label.pack()
# labelConf(label,"123")
# default_font = tkF.nametofont("TkDefaultFont")
# default_font.configure(size=30)
# root.option_add("*Font", default_font)

# L1 = tk.Label(root, text="L1", bg="green")
# L2 = tk.Label(root, text="L1", bg="red")
# L3 = tk.Label(root, text="L1", bg="blue")

# L1.grid(row=0, column=0, columnspan=2)
# L2.grid(row=1, column=0)
# L3.grid(row=1, column=1)

# def echo_data(jakis_obiekt):
# 	tkMB.showinfo("Message", jakis_obiekt.get())
# x=0
# def add(ent, y):
# 	global x
# 	x+=y
# 	ent.delete(0,'end')
# 	ent.insert(tk.END, str(x))



# e1 = tk.Entry(root)
# e1.grid(row=0,column=0,columnspan=2)

# bt = tk.Button(root, text="1",command=lambda: add(e1,1))
# bt.grid(row = 1, column = 0)

# bt2 = tk.Button(root, text="2",command=lambda: add(e1,2))
# bt2.grid(row = 1, column = 1)

# def stateChange(var1):
# 	print(var1.get())

# var1 = tk.BooleanVar()
# cb1 = tk.Checkbutton(root, text="T1", variable=var1, command=lambda:stateChange(var1))
# cb1.grid(column = 0, row=0)

# var2 = tk.BooleanVar()
# cb2 = tk.Checkbutton(root, text="T2", variable=var2, command=lambda:stateChange(var2))
# cb2.grid(column = 1, row=0)


# v = tk.IntVar()

# def ReadV():
# 	print (v.get())

# rb1 = tk.Radiobutton(root, text="1", variable = v, value = 1, command=ReadV)
# rb1.grid(column=0, row=0)
# rb2 = tk.Radiobutton(root, text="2", variable = v, value = 2, command=ReadV)
# rb2.grid(column=0, row=1)

# v2 = tk.IntVar()

# rb3 = tk.Radiobutton(root, text="3", variable = v2, value = 3, command=ReadV)
# rb3.grid(column=1, row=0)
# rb4 = tk.Radiobutton(root, text="4", variable = v2, value = 4, command=ReadV)
# rb4.grid(column=1, row=1)

# scroll = tk.Scrollbar(root)

# ta = tk.Text(root, height=10, width=50)
# ta.pack(side = tk.LEFT, fill=tk.Y)
# scroll.pack(side=tk.RIGHT,fill=tk.Y)

# ta.config(yscrollcommand=scroll.set)
# scroll.config(command=ta.yview)
# ta.insert(tk.END,"ttt")

cnv = tk.Canvas(root, width=200,height=100)
cnv.pack()
cnv.create_rectangle(50,20,150,80,fill="dark green")
cnv.create_rectangle(65,35,135,65,fill="#FF124F")
cnv.create_line(0,0,50,20,fill="#000011",width=3)
cnv.create_line(0,100,50,80,fill="#000011",width=3)
cnv.create_line(150,80,200,100,fill="#000011",width=3)
root.mainloop()