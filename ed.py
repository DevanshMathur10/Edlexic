from tkinter import *
from tkvideo import tkvideo
from fruits import fruits

def edwin():

    root1=Toplevel()
    root1.geometry("360x640")
    root1.title("EDLEXIC")

    imglbl1=Label(root1)
    imglbl1.place(x=0, y=0, relwidth=1, relheight=1)
    player1 = tkvideo("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/mainwindowbackvid1.mp4", imglbl1,loop = 1, size = (360,640))
    player1.play()

    def themes():

        frame3=Frame(root1,bg='#cab5e8', relief=RAISED)
        frame3.place(x=180,y=250,anchor='center')

        fb=Button(frame3,text="FRUITS",bg='#712b75',fg='#ffffff',font=("Helvetica",12,'bold'),command=fruits)
        fb.grid(row=0,column=0,padx=10,pady=5,ipadx=40,ipady=30)

        fb=Button(frame3,text="PLANETS",bg='#712b75',fg='#ffffff',font=("Helvetica",12,'bold'))
        fb.grid(row=0,column=1,padx=10,pady=5,ipadx=33,ipady=30)

        fb=Button(frame3,text="ANIMALS",bg='#712b75',fg='#ffffff',font=("Helvetica",12,'bold'))
        fb.grid(row=1,column=0,padx=10,pady=5,ipadx=33,ipady=30)

        fb=Button(frame3,text="VEGETABLES",bg='#712b75',fg='#ffffff',font=("Helvetica",12,'bold'))
        fb.grid(row=1,column=1,padx=10,pady=5,ipadx=16,ipady=30)

    frame2=Frame(root1,bg='#decafa', relief=RAISED)
    frame2.place(x=180,y=250,anchor='center')

    fb=Button(frame2,text="LEARN",bg='#9e59ff',fg='#ffffff',font=("Helvetica",12,'bold'),command=themes)
    fb.grid(row=0,column=0,padx=10,pady=5,ipadx=40,ipady=30)

    fb=Button(frame2,text="PRACTICE",bg='#9e59ff',fg='#ffffff',font=("Helvetica",12,'bold'))
    fb.grid(row=0,column=1,padx=10,pady=5,ipadx=32,ipady=30)

    fb=Button(frame2,text="TEST",bg='#9e59ff',fg='#ffffff',font=("Helvetica",12,'bold'))
    fb.grid(row=1,column=0,padx=10,pady=5,ipadx=47,ipady=30)

    fb=Button(frame2,text="SOURCES",bg='#9e59ff',fg='#ffffff',font=("Helvetica",12,'bold'))
    fb.grid(row=1,column=1,padx=10,pady=5,ipadx=33,ipady=30)

    root1.mainloop()

#edwin()