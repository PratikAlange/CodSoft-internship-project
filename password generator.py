# Password generator
import tkinter as tk
import random
root=tk.Tk()
root.title('Password Generator')
root.geometry('450x400+450+170')
root.minsize(450,400)
root.maxsize(450,400)

def generate():
    password_generator='''abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/-+_'''
    password=''
    length=int(e1.get())
    for i in range(length):
        a=random.randint(0,len(password_generator)-1)
        password+=password_generator[a]
    e2.delete(0,tk.END)
    e2.insert(tk.END,password)
       
root['bg']='cyan'
l1=tk.Label(root,text='Password Generator',bg='black',font='CenturyGothic 26 bold',fg='white')
l1.place(x=49,y=10)

l2=tk.Label(root,text='Password Length',font='CenturyGothic 14 bold',fg='black',bg='cyan')
l2.place(x=55,y=90)

e1=tk.Entry(root,width=10,font='CenturyGothic 12',fg='black',borderwidth=3)
e1.place(x=235,y=92)

b1=tk.Button(text='Generate',borderwidth=3,font='CenturyGothic 14 bold',bg='black',fg='white',command=generate)
b1.place(x=170,y=165)

e2=tk.Entry(root,font='CenturyGothic 14 bold',width=17,bd=0,bg='cyan')
e2.place(x=132.5,y=250)
root.mainloop()



















