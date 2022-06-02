from tkinter import * 
win = Tk()  
c = Canvas(win,width=300,height=200,borderwidth=0,highlightthickness=0,bg="yellow")
c.pack(expand=True,fill=BOTH) 
x = 0 
y = 0
spd1 = 40 
spd2 = 70 
red_box = c.create_rectangle(x,95,x+20,115,fill='red',width=0)
 
def update(): 
    global x,y
    global spd1,spd2
    win.after(20,update)
    c.moveto(red_box,x,y)
    x+=spd1
    y+=spd2
    if x >= c.winfo_width()-10 or x <= 0:
        spd1*=-1
    if y >= c.winfo_height()-10 or y <= 0:
        spd2*=-1
win.after(2,update)
win.mainloop()