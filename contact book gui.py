# Contact Book gui
import mysql.connector
import tkinter.messagebox
import tkinter as tk

cn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pratik@23',
    database='contact_book')
root=tk.Tk()
root.title('Contact Book')
root.geometry('600x380+300+100')
root.minsize(600,380)
root.maxsize(600,380)
# Creating Labels
heading=tk.Label(root,text='Contact Book',font=('Brush Script MT',26,'bold italic')).place(x=220,y=17)
l1=tk.Label(root,text='Enter Name',font=('Arial Rounded MT Bold',14)).place(x=80,y=85)
l2=tk.Label(root,text='Enter Phone no',font=('Arial Rounded MT Bold',14)).place(x=80,y=115)
l3=tk.Label(root,text='Enter email',font=('Arial Rounded MT Bold',14)).place(x=80,y=145)
l4=tk.Label(root,text='Enter Address',font=('Arial Rounded MT Bold',14)).place(x=80,y=175)
# Creating Entry fields
e1=tk.Entry(root,font=('Century Gothic',12),width=30)
e1.place(x=280,y=85)

e2=tk.Entry(root,font=('Century Gothic',12),width=30)
e2.place(x=280,y=115)

e3=tk.Entry(root,font=('Century Gothic',12),width=30)
e3.place(x=280,y=145)

e4=tk.Entry(root,font=('Century Gothic',12),width=30)
e4.place(x=280,y=175)

def save():
    cur=cn.cursor()
    try:
        s='insert into book (name,phone,email,address) values (%s,%s,%s,%s)'
        t=(e1.get(),e2.get(),e3.get(),e4.get())
        cur.execute(s,t)
        tkinter.messagebox.showinfo(message='Contact successfully added.')
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
        e3.delete(0,tk.END)
        e4.delete(0,tk.END)
        cn.commit()
    except:
        tkinter.messagebox.showerror(message='Unable to add')
        
b1=tk.Button(root,fg='black',text='Save',font=('Arial Rounded MT Bold',12),command=save).place(x=75,y=220)
b2=tk.Button(root,fg='black',text='Cancel',font=('Arial Rounded MT Bold',12),command=root.destroy).place(x=150,y=220)

def search():
    search_win=tk.Tk()
    search_win.title('Search By Name')
    search_win.geometry('500x380+350+100')
    search_win.configure(bg='light grey')
    l1=tk.Label(search_win,text='Search By Name',font=('Brush Script MT',26,'bold italic'),bg='light grey').place(x=150,y=8)
    l2=tk.Label(search_win,text='Enter Name',font=('Arial Rounded MT Bold',14),bg='light grey').place(x=30,y=70)
    e1=tk.Entry(search_win,font=('Century Gothic',12),width=23)
    e1.place(x=160,y=72)
    
    def search_record():
        try:
            cur=cn.cursor()
            s="select name,phone,email,address from book where name=%s"
            t=(e1.get(),)
            cur.execute(s,t)
            result=cur.fetchone()
            e2.insert(tk.END,result[0])
            e3.insert(tk.END,result[1])
            e4.insert(tk.END,result[2])
            e5.insert(tk.END,result[3])
        except:
            tkinter.messagebox.showerror(title='Error',message='Unable to fetch record.')
            
    b1=tk.Button(search_win,text='Search',font=('Arial Rounded MT Bold',12),bg='light grey',command=search_record).place(x=30,y=120)
    l2=tk.Label(search_win,text='Name',font=('Arial Rounded MT Bold',14),bg='light grey').place(x=30,y=175)
    l3=tk.Label(search_win,text='Phone No',font=('Arial Rounded MT Bold',14),bg='light grey').place(x=30,y=210)
    l4=tk.Label(search_win,text='Email',font=('Arial Rounded MT Bold',14),bg='light grey').place(x=30,y=245)
    l5=tk.Label(search_win,text='Address',font=('Arial Rounded MT Bold',14),bg='light grey').place(x=30,y=280)

    e2=tk.Entry(search_win,font=('Century Gothic',12),width=27,bg='light grey',bd=0)
    e2.place(x=165,y=175)
    e3=tk.Entry(search_win,font=('Century Gothic',12),width=27,bg='light grey',bd=0)
    e3.place(x=165,y=210)
    e4=tk.Entry(search_win,font=('Century Gothic',12),width=27,bg='light grey',bd=0)
    e4.place(x=165,y=245)
    e5=tk.Entry(search_win,font=('Century Gothic',12),width=27,bg='light grey',bd=0)
    e5.place(x=165,y=280)
b3=tk.Button(root,text='Search',font=('Arial Rounded MT Bold',12),command=search).place(x=75,y=300)
def update():
    update_win=tk.Tk()
    update_win.title('Update')
    update_win.geometry('240x160+30+100')
    update_win.minsize(240,160)
    update_win.maxsize(240,160)
    
    def update_phone():
        update_phone_win=tk.Tk()
        update_phone_win.title('Update Phone')
        update_phone_win.geometry('350x230+30+100')
        update_phone_win.minsize(350,230)
        update_phone_win.maxsize(350,230)
        l1=tk.Label(update_phone_win,text='Update Phone',font=('Brush Script MT',26,'bold italic')).place(x=88,y=5)
        l2=tk.Label(update_phone_win,text='Enter Name',font=('Arial Rounded MT Bold',14)).place(x=8,y=70)
        e1=tk.Entry(update_phone_win,font=('Century Gothic',12),width=22)
        e1.place(x=130,y=73)
        l3=tk.Label(update_phone_win,text='Enter Phone',font=('Arial Rounded MT Bold',14)).place(x=8,y=120)
        e2=tk.Entry(update_phone_win,font=('Century Gothic',12),width=22)
        e2.place(x=130,y=120)
        
        def update_phone_record():
            cur=cn.cursor()
            s="update book set phone=%s where name=%s"
            t=(e2.get(),e1.get())
            cur.execute(s,t)
            tkinter.messagebox.showinfo(title='Update Phone',message='Phone no updated successfully.')
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            cn.commit()
            update_phone_win.destroy()
        b1=tk.Button(update_phone_win,text='Update',font=('Arial Rounded MT Bold',12),command=update_phone_record).place(x=30,y=170)

    b1=tk.Button(update_win,text='Update Phone',font=('Arial Rounded MT Bold',12),command=update_phone).place(x=45,y=15)


    def update_email():
        update_email_win=tk.Tk()
        update_email_win.title('Update Email')
        update_email_win.geometry('350x230+30+100')
        update_email_win.minsize(350,230)
        update_email_win.maxsize(350,230)
        l1=tk.Label(update_email_win,text='Update Email',font=('Brush Script MT',26,'bold italic')).place(x=88,y=5)
        l2=tk.Label(update_email_win,text='Enter Name',font=('Arial Rounded MT Bold',14)).place(x=8,y=70)
        e1=tk.Entry(update_email_win,font=('Century Gothic',12),width=22)
        e1.place(x=130,y=73)
        l3=tk.Label(update_email_win,text='Enter Email',font=('Arial Rounded MT Bold',14)).place(x=8,y=120)
        e2=tk.Entry(update_email_win,font=('Century Gothic',12),width=22)
        e2.place(x=130,y=120)
        def update_email_record():
            cur=cn.cursor()
            s="update book set email=%s where name=%s"
            t=(e2.get(),e1.get())
            cur.execute(s,t)
            tkinter.messagebox.showinfo(title='Update Email',message='Email updated successfully.')
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            cn.commit()
            update_email_win.destroy()
        b1=tk.Button(update_email_win,text='Update',font=('Arial Rounded MT Bold',12),command=update_email_record).place(x=30,y=170)
        
    b2=tk.Button(update_win,text='Update Email',font=('Arial Rounded MT Bold',12),command=update_email).place(x=45,y=60)

    def update_address():
        update_address_win=tk.Tk()
        update_address_win.title('Update Address')
        update_address_win.geometry('350x230+30+100')
        update_address_win.minsize(350,230)
        update_address_win.maxsize(350,230)
        l1=tk.Label(update_address_win,text='Update Address',font=('Brush Script MT',26,'bold italic')).place(x=75,y=5)
        l2=tk.Label(update_address_win,text='Enter Name',font=('Arial Rounded MT Bold',13)).place(x=8,y=70)
        e1=tk.Entry(update_address_win,font=('Century Gothic',12),width=20)
        e1.place(x=133,y=73)
        l3=tk.Label(update_address_win,text='Enter Address',font=('Arial Rounded MT Bold',13)).place(x=8,y=120)
        e2=tk.Entry(update_address_win,font=('Century Gothic',12),width=20)
        e2.place(x=133,y=120)
        def update_address_record():
            cur=cn.cursor()
            s="update book set address=%s where name=%s"
            t=(e2.get(),e1.get())
            cur.execute(s,t)
            tkinter.messagebox.showinfo(title='Update Address',message='Address updated successfully.')
            e1.delete(0,tk.END)
            e2.delete(0,tk.END)
            cn.commit()
            update_address_win.destroy()
        b1=tk.Button(update_address_win,text='Update',font=('Arial Rounded MT Bold',12),command=update_address_record).place(x=30,y=170)
    b3=tk.Button(update_win,text='Update Address',font=('Arial Rounded MT Bold',12),command=update_address).place(x=45,y=105)
    
    
b4=tk.Button(root,text='Update',font=('Arial Rounded MT Bold',12),command=update).place(x=170,y=300)

def delete():
    delete_win=tk.Tk()
    delete_win.title('Delete')
    delete_win.geometry('350x190+930+100')
    delete_win.minsize(350,190)
    delete_win.maxsize(350,190)
    l1=tk.Label(delete_win,text='Delete Record',font=('Brush Script MT',26,'bold italic')).place(x=88,y=5)
    l2=tk.Label(delete_win,text='Enter Name',font=('Arial Rounded MT Bold',14)).place(x=8,y=70)
    e1=tk.Entry(delete_win,font=('Century Gothic',12),width=22)
    e1.place(x=130,y=73)
    def delete_record():
        cur=cn.cursor()
        s="delete from book where name=%s"
        t=(e1.get(),)
        cur.execute(s,t)
        tkinter.messagebox.showinfo(message='Record deleted.')
        e1.delete(0,tk.END)
        cn.commit()
        
    b1=tk.Button(delete_win,text='Delete',font=('Arial Rounded MT Bold',12),command=delete_record).place(x=30,y=130)
    
b5=tk.Button(root,text='Delete',font=('Arial Rounded MT Bold',12),command=delete).place(x=270,y=300)

def view_contact_book():
    cur=cn.cursor()
    s="select*from book"
    cur.execute(s)
    result=cur.fetchall()
    for record in result:
        print(record)
b6=tk.Button(root,text='View',font=('Arial Rounded MT Bold',12),command=view_contact_book).place(x=360,y=300)
root.mainloop()
















