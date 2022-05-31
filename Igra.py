from tkinter import * 
win = Tk()  
c = Canvas(win,width=300,height=200,borderwidth=0,highlightthickness=0,bg="yellow")
c.pack(expand=True,fill=BOTH) 
x = 0 
spd = 4 
red_box = c.create_rectangle(x,95,x+10,105,fill="red",width=0) 
win.mainloop()