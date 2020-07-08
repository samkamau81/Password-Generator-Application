import _tkinter
from string import punctuation, ascii_letters, digits
import random
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()

def create_passw(length):
    try:
        length=int(length)
        all=punctuation+ascii_letters+digits
        secure_random=random.SystemRandom()
        password="".join(secure_random.choice(all) for i in range(length))
        e2.insert (10, password)
    except ValueError:
        e2.insert(10, "Enter Numeric Value !")


def clear():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)


def exit():
    ex = messagebox.askyesno ("Password Generator", "Confirm if you want to exit")
    if ex > 0:
        root.quit ()
        return



root.geometry('600x350+0+0')
root.configure(bg='violet')
try:
    photo = tk.PhotoImage (file="key.ico")
    root.iconphoto (False, photo)
except _tkinter.TclError:
    pass
size=tk.StringVar()

L1=tk.Label(root,text="PASSWORD GENERATOR",font=('arial',20,'bold','underline'),bg='violet')
L1.grid(row=0, column=0)
L2=tk.Label(root,text="Enter the Length of intended password:",font=('lucida handwriting',10),bg='violet')
L2.grid(row=3, column=0)
e1=tk.Entry(root,text=size)
e1.grid(row=3, column=1)
b1=tk.Button(root,text="PASSWORD =",command=lambda:create_passw(e1.get()))
b1.grid(row=4, column=0,padx=10,pady=1)
e2=tk.Entry(root)

e2.grid(row=4, column=1)
b2=tk.Button(root,text="CLEAR",command=lambda:clear())
b2.grid(row=5, column=0,padx=10,pady=10)
b3=tk.Button(root,text="EXIT",command=lambda:exit())
b3.grid(row=5, column=1,padx=10,pady=10)
root.mainloop()









