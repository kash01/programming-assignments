from tkinter import *
from tkinter import messagebox

root = Tk()
root.minsize(200,100)
root.resizable(True,False)
global e1,e2,usercheck,passcheck
usercheck = passcheck = False

def usertext(event):
	global usercheck
	usercheck = True
	e1.delete(0,END)
	
def passtext(event):
	global passcheck
	passcheck = True
	e2.delete(0,END)
	
def login(event = None):
	if usercheck == True and passcheck == True:
		l1.configure(text = "Login Successful !")
	else:
		messagebox.showerror("Invalid login","Please fill the username and password fields")
	

l1 = Label(root, text = "Hello !",font='Arial 12 bold', bg = 'lightblue')
l1.pack(padx = 20,pady = 20, ipadx = 20, ipady = 5, fill = X)
e1=Entry(root)
e1.pack(padx = 20,pady = 20, ipadx = 20, ipady = 5, fill = X)
e1.insert(0,"Enter Name here")
e1.bind("<Button -1>",usertext)
e2=Entry(root)
e2.pack(padx = 20,pady = 20, ipadx = 20, ipady = 5, fill = X)
e2.insert(0,"Enter Password here")
e2.bind("<Button -1>",passtext)
e2.bind("<Return>",login)
b1 = Button(root, text = 'Login', command = login)
b1.pack(padx = 20,pady = 20, ipadx = 20, ipady = 5)
root.mainloop()