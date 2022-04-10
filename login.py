from tkinter import *
from tkvideo import tkvideo
from emailsender import sendmsg
from emailpasssender import sendpass,p
from ed import edwin

root=Tk()
root.geometry("360x640")
root.title("LOGIN")
imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/backvid.mp4", imglbl,loop = 1, size = (360,640))
player.play()

def signin():
    frame1=Frame(root,bg='#000000', relief=RAISED)
    frame1.place(x=180,y=220,anchor='center')

    NAME=Label(frame1,text="Name",background="#000000",fg='white', font=('Book Antiqua', 11))
    NAME.grid(row=0,column=0,padx=8,pady=(5,0))
    password=Label(frame1,text="Pass",background="#000000",fg='white', font=('Book Antiqua', 11))
    password.grid(row=1,column=0)

    NAME_box=Entry(frame1,width=35,borderwidth=2)
    NAME_box.grid(row=0,column=1,pady=(5,0),padx=10)
    pass_box=Entry(frame1,width=35,borderwidth=2,show="•")
    pass_box.grid(row=1,column=1)

    checkbtn=Button(frame1,text="SIGN IN",command=edwin)
    checkbtn.grid(row=2,column=1,columnspan=2,padx=10,pady=5,ipadx=45)

def signup():

    def submitpass():
        if otp_box.get()==p:
            passshow=Label(frame1,text=" CORRECT OTP ",background="#000000",fg='white', font=('arial', 9))
            passshow.grid(row=5,column=1,columnspan=2,padx=8)
            signbtn=Button(frame1,text="SIGN UP",command=lambda: [sendmsg(email_box.get(),NAME_box.get()),edwin()],state=ACTIVE)
            signbtn.grid(row=7,column=1,columnspan=2,padx=10,pady=5,ipadx=45)
            
        else:
            passshow=Label(frame1,text="INCORRECT OTP",background="#000000",fg='white', font=('arial', 9))
            passshow.grid(row=5,column=1,columnspan=2,padx=8)

    frame1=Frame(root,bg='#000000', relief=RAISED)
    frame1.place(x=180,y=220,anchor='center')

    NAME=Label(frame1,text="Name",background="#000000",fg='white', font=('Book Antiqua', 11))
    NAME.grid(row=0,column=0,padx=8,pady=(5,0))
    email=Label(frame1,text="Email",background="#000000",fg='white', font=('Book Antiqua', 11))
    email.grid(row=1,column=0,padx=8,pady=(5,0))
    otp=Label(frame1,text="OTP",background="#000000",fg='white', font=('Book Antiqua', 11))
    otp.grid(row=3,column=0,pady=(5,0))
    password=Label(frame1,text="Pass",background="#000000",fg='white', font=('Book Antiqua', 11))
    password.grid(row=6,column=0,pady=(5,0))

    NAME_box=Entry(frame1,width=35,borderwidth=2)
    NAME_box.grid(row=0,column=1,pady=(5,0),padx=10)
    email_box=Entry(frame1,width=35,borderwidth=2)
    email_box.grid(row=1,column=1,pady=(5,0),padx=10)
    otp_box=Entry(frame1,width=35,borderwidth=2,show="•")
    otp_box.grid(row=3,column=1,pady=(5,0),padx=10)
    pass_box=Entry(frame1,width=35,borderwidth=2,show="•")
    pass_box.grid(row=6,column=1,pady=(5,0),padx=10)

    sendbtn=Button(frame1,text="SEND OTP",command=lambda: sendpass(str(email_box.get())))
    sendbtn.grid(row=2,column=1,columnspan=2,padx=10,pady=5,ipadx=50)

    checkbtn=Button(frame1,text="CHECK OTP",command=submitpass)
    checkbtn.grid(row=4,column=1,columnspan=2,padx=10,pady=5,ipadx=45)

    signbtn=Button(frame1,text="SIGN UP",command=lambda: sendmsg(email_box.get(),NAME_box.get()),state=DISABLED)
    signbtn.grid(row=7,column=1,columnspan=2,padx=10,pady=5,ipadx=45)

frame=Frame(root,bg='#000000', relief=RAISED)
frame.place(x=180,y=220,anchor='center')

checkbtn1=Button(frame,text="SIGN IN",command=signin)
checkbtn1.grid(row=0,column=0,padx=10,pady=5,ipadx=45)

checkbtn2=Button(frame,text="SIGN UP",command=signup)
checkbtn2.grid(row=1,column=0,padx=10,pady=5,ipadx=45)

root.mainloop()