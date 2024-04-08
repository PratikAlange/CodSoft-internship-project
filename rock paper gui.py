# Rock Paper Scissor
import tkinter as tk
import random

root=tk.Tk()
root.title('Rock Paper Scissor')
root.geometry('500x400+450+170')
root.configure(bg='#37FF64')

head=tk.Label(root,text='Rock Paper Scissor',font=('Brush Script MT',30,'bold italic'),bg='#37FF64').place(x=110,y=5)

def click(event):
    list1=['Rock','Paper','Scissor']
    computer=random.choice(list1)
    text=event.widget.cget('text')
    if text==computer:
        result.delete(0,tk.END)
        result.insert(tk.END,"It's Tie")
        
    elif text=='Rock' and computer=='Paper':
         result.delete(0,tk.END)
         result.insert(tk.END,"You Lose")
    elif text=='Rock' and computer=='Scissor':
        result.delete(0,tk.END)
        result.insert(tk.END,"You Win")
    elif text=='Paper' and computer=='Rock':
        result.delete(0,tk.END)
        result.insert(tk.END,"You Win")
    elif text=='Paper' and computer=='Scissor':
        result.delete(0,tk.END)
        result.insert(tk.END,"You Lose")
    elif text=='Scissor' and computer=='Rock':
        result.delete(0,tk.END)
        result.insert(tk.END,"You Lose")
    elif text=='Scissor' and computer=='Paper':
        result.delete(0,tk.END)
        result.insert(tk.END,"You Win")
        
         

r_frame=tk.Frame(root,bg='black',borderwidth=3,relief=tk.SUNKEN)
r_frame.place(x=40,y=135)
rock=tk.Button(r_frame,text='Rock',fg='black',font=('Arial Rounded MT Bold',14),width=8)
rock.grid(row=180,column=40)
rock.bind('<Button-1>',click)

p_frame=tk.Frame(root,bg='black',borderwidth=3,relief=tk.SUNKEN)
p_frame.place(x=195,y=135)
paper=tk.Button(p_frame,text='Paper',fg='black',font=('Arial Rounded MT Bold',14),width=8)
paper.grid(row=180,column=40)
paper.bind('<Button-1>',click)

s_frame=tk.Frame(root,bg='black',borderwidth=3,relief=tk.SUNKEN)
s_frame.place(x=350,y=135)
scissor=tk.Button(s_frame,text='Scissor',fg='black',font=('Arial Rounded MT Bold',14),width=8)
scissor.grid(row=180,column=40)
scissor.bind('<Button-1>',click)

result=tk.Entry(root,width=10,font=('Arial Rounded MT Bold',24),bd=0,bg='#37FF64')
result.place(x=185,y=270)

root.mainloop()
