import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkF
import tkinter.messagebox as tkMb
import tkinter.filedialog as tkf

root = tk.Tk()
root.maxsize(width=1500, height=800)
root.minsize(width=1500, height=800)

a=30

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=10)
root.option_add("*Font", default_font)

ta = tk.Text(root,height=10, width=50)
ta.grid(row=1,column=0,columnspan=4,sticky = tk.W+tk.E+tk.N)
scroll = tk.Scrollbar(root)
scroll.grid(row=1,column=4,columnspan=4,sticky = tk.W+tk.E+tk.N)
def odtworz():
    file_path = tkf.askopenfilename()
    F = open(file_path,"r")
    ta.insert(tk.END,F.read())
def zapisz():
    file_path = tkf.asksaveasfilename()
    filer = open(file_path,"w")
    filer.write(ta.get())
def zmnR():
    global a
    a-=1
    ta.config(font=("courier",a))
def zwnR():
    global a
    a+=1
    ta.config(font=("courier",a))   
bt = tk.Button(root,text = "Odtworz plik",command = lambda: odtworz())
bt.grid(row = 0,column=0,sticky = tk.W+tk.E)
bt1 = tk.Button(root,text = "Zapisz plik",command = lambda: zapisz())
bt1.grid(row = 0,column=1,sticky = tk.W+tk.E)
bt2 = tk.Button(root,text = "Zwieksz rozmiar czcionki",command = lambda: zwnR())
bt2.grid(row = 0,column=2,sticky = tk.W+tk.E)
bt3 = tk.Button(root,text = "Zmniejsz rozmiar czcionki",command = lambda: zmnR())
bt3.grid(row = 0,column=3,sticky = tk.W+tk.E)
ta.config(yscrollcommand=scroll.set)
scroll.config(command=ta.yview)
root.mainloop()
