# simple calculator

import tkinter as tk

root=tk.Tk()
root.title('Simple Calculator')
root.geometry('350x300+450+170')
root.minsize(350,300)
root.maxsize(350,300)

tk.Label(root,text='Calculator',font=('Century Gothic',26,'bold')).place(x=80,y=0)

l1=tk.Label(root,text='Number',font=('Century Gothic',14))
l1.place(x=60,y=60)

l2=tk.Label(root,text='Number',font=('Century Gothic',14))
l2.place(x=60,y=90)

l3=tk.Label(root,text='Result',font=('Century Gothic',14))
l3.place(x=60,y=120)

e1=tk.Entry(root,width=10,font=('Century Gothic',12))
e1.place(x=155,y=62)

e2=tk.Entry(root,width=10,font=('Century Gothic',12))
e2.place(x=155,y=92)

e3=tk.Entry(root,width=10,font=('Century Gothic',12))
e3.place(x=155,y=122)

def add():
    num1=eval(e1.get())
    num2=eval(e2.get())
    result=num1+num2
    e3.delete(0,tk.END)
    e3.insert(tk.END,result)
def subtract():
    num1=eval(e1.get())
    num2=eval(e2.get())
    result=num1-num2
    e3.delete(0,tk.END)
    e3.insert(tk.END,result)

def multiply():
    num1=eval(e1.get())
    num2=eval(e2.get())
    result=num1*num2
    e3.delete(0,tk.END)
    e3.insert(tk.END,result)

def divide():
    num1=eval(e1.get())
    num2=eval(e2.get())
    result=num1/num2
    e3.delete(0,tk.END)
    e3.insert(tk.END,f'{result:.2}')
#Button
b1=tk.Button(root,font=('Century Gothic',10),width=8,text='Add',fg='black',borderwidth=4,command=add).place(x=30,y=180)
b2=tk.Button(root,font=('Century Gothic',10),width=8,text='Subtract',fg='black',borderwidth=4,command=subtract).place(x=137,y=180)
b3=tk.Button(root,font=('Century Gothic',10),width=8,text='Multiply',fg='black',borderwidth=4,command=multiply).place(x=240,y=180)
b4=tk.Button(root,font=('Century Gothic',10),width=8,text='Divide',fg='black',borderwidth=4,command=divide).place(x=85,y=229)
b5=tk.Button(root,font=('Century Gothic',10),width=8,text='Quit',fg='red',borderwidth=4,command=root.destroy).place(x=192,y=229)
root.mainloop()





































