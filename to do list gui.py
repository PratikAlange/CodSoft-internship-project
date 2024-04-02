# to - do - list gui

import tkinter as tk
import tkinter.messagebox
root=tk.Tk()
root.title('To Do List')
root.geometry('450x400+450+170')
root.minsize(450,400)
root.maxsize(450,400)

l1=tk.Label(root,text='To Do List',font=('Brush Script MT',26,'bold italic')).place(x=150,y=2)
l2=tk.Label(root,text='Focus',font=('Bradley Hand ITC',14)).place(x=198,y=70)
l3=tk.Label(root,text='Work Hard',font=('Bradley Hand ITC',14)).place(x=173,y=95)
l4=tk.Label(root,text='Be Creative',font=('Bradley Hand ITC',14)).place(x=173,y=120)
l5=tk.Label(root,text='Open Your Mind',font=('Bradley Hand ITC',14)).place(x=150,y=143)
l6=tk.Label(root,text='Enjoy The Little Things',font=('Bradley Hand ITC',14)).place(x=118,y=168)
l7=tk.Label(root,text='Put In 100% Effort',font=('Bradley Hand ITC',14)).place(x=145,y=193)
l8=tk.Label(root,text='Take Chances',font=('Bradley Hand ITC',14)).place(x=169,y=216)
l9=tk.Label(root,text='Smile More',font=('Bradley Hand ITC',14)).place(x=177,y=239)
l10=tk.Label(root,text='Breathe',font=('Bradley Hand ITC',14)).place(x=194,y=260)


def create():
    
    create=tk.Tk()
    create.title('To Do List')
    create.geometry('450x300+450+170')
    create.minsize(450,300)
    create.maxsize(450,300)
    e1=tk.Entry(create,width=20,font=('Century Gothic',14),borderwidth=2)
    e1.place(x=114,y=60)
    
    to_do_list=[]
    def add():
        value=e1.get()
        to_do_list.append(value)
        e1.delete(0,tk.END)
        
        
    b1=tk.Button(create,text='Add',width=7,font=('Brush Script MT',14),borderwidth=2,command=add).place(x=190,y=110)

    def update():
        update=tk.Tk()
        update.title('Update')
        update.geometry('350x220+50+170')
        update.minsize(350,220)
        update.maxsize(350,220)
        l1=tk.Label(update,text='Old Task',font=('Brush Script MT',14)).place(x=25,y=40)
        l2=tk.Label(update,text='New Task',font=('Brush Script MT',14)).place(x=25,y=80)
        e1=tk.Entry(update,width=17,font=('Century Gothic',14),borderwidth=2)
        e1.place(x=120,y=40)
        e2=tk.Entry(update,width=17,font=('Century Gothic',14),borderwidth=2)
        e2.place(x=120,y=80)
        def save():
            old_value=e1.get()
            new_value=e2.get()
            if old_value in to_do_list:
                a=to_do_list.index(old_value)
                to_do_list.insert(a,new_value)
                del to_do_list[a+1]
                e3.insert(tk.END,'Task added.')
            else:
                e3.insert(tk.END,'No such task.')
           
            
        b1=tk.Button(update,text='Save',width=7,font=('Brush Script MT',14),borderwidth=2,command=save).place(x=40,y=140)
        e3=tk.Entry(update,font=('Arial',12,'bold'),width=13,bd=0,bg='#d9d9d9')
        e3.place(x=135,y=148)
    b2=tk.Button(create,text='Update',width=7,font=('Brush Script MT',14),borderwidth=2,command=update).place(x=110,y=215)
    def track():
        if len(to_do_list)==0:
            tkinter.messagebox.showinfo(title='Track',message='Empty list.')
        else:
            tkinter.messagebox.showinfo(title='track',message=f'{to_do_list}')        

    b3=tk.Button(create,text='Track List',width=9,font=('Brush Script MT',14),borderwidth=2,command=track).place(x=250,y=215)

  
b1=tk.Button(root,text='Create',width=7,font=('Brush Script MT',14),borderwidth=2,command=create).place(x=190,y=305)


root.mainloop()
















