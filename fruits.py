from tkinter import *
from tts import speak
from PIL import Image,ImageTk

def fruits():
    root2=Toplevel()
    root2.configure(bg='#e2cffc')

    myimg1=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/apple.jpg")
    myimg2=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/bananas.jpg")
    myimg3=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/guava.jpg")
    myimg4=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/orange.jpg")
    myimg5=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/kiwi.jpg")
    myimg6=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/strawberries.jpg")
    myimg7=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/pineapple.jpg")
    myimg8=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/grape.jpg")

    resize1=myimg1.resize((150,100),Image.ANTIALIAS)
    resize2=myimg2.resize((150,100),Image.ANTIALIAS)
    resize3=myimg3.resize((150,100),Image.ANTIALIAS)
    resize4=myimg4.resize((150,100),Image.ANTIALIAS)
    resize5=myimg5.resize((150,100),Image.ANTIALIAS)
    resize6=myimg6.resize((150,100),Image.ANTIALIAS)
    resize7=myimg7.resize((150,100),Image.ANTIALIAS)
    resize8=myimg8.resize((150,100),Image.ANTIALIAS)

    newimg1=ImageTk.PhotoImage(resize1)
    newimg2=ImageTk.PhotoImage(resize2)
    newimg3=ImageTk.PhotoImage(resize3)
    newimg4=ImageTk.PhotoImage(resize4)
    newimg5=ImageTk.PhotoImage(resize5)
    newimg6=ImageTk.PhotoImage(resize6)
    newimg7=ImageTk.PhotoImage(resize7)
    newimg8=ImageTk.PhotoImage(resize8)

    my_label=Label(root2,image=newimg1)
    my_label.grid(row=0,column=0,pady=(5,0))
    fb=Button(root2,text="APPLE",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("A"),speak("P"),speak("P"),speak("L"),speak("E"),speak("APPLE")])
    fb.grid(row=1,column=0,padx=10,pady=5,ipadx=42)

    my_label=Label(root2,image=newimg2)
    my_label.grid(row=0,column=1,pady=(5,0))
    fb=Button(root2,text="BANANA",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("B"),speak("A"),speak("N"),speak("A"),speak("N"),speak("A"),speak("BANANA")])
    fb.grid(row=1,column=1,padx=10,pady=5,ipadx=35)

    my_label=Label(root2,image=newimg3)
    my_label.grid(row=2,column=0)
    fb=Button(root2,text="GUAVA",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("G"),speak("U"),speak("A"),speak("V"),speak("A"),speak("GUAVA")])
    fb.grid(row=3,column=0,padx=10,pady=5,ipadx=40)

    my_label=Label(root2,image=newimg4)
    my_label.grid(row=2,column=1)
    fb=Button(root2,text="ORANGE",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("O"),speak("R"),speak("A"),speak("N"),speak("G"),speak("E"),speak("ORANGE")])
    fb.grid(row=3,column=1,padx=10,pady=5,ipadx=34)

    my_label=Label(root2,image=newimg5)
    my_label.grid(row=4,column=0)
    fb=Button(root2,text="KIWI",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("K"),speak("I"),speak("W"),speak("I"),speak("KIWI")])
    fb.grid(row=5,column=0,padx=10,pady=5,ipadx=51)

    my_label=Label(root2,image=newimg6)
    my_label.grid(row=4,column=1)
    fb=Button(root2,text="STRAWBERRIES",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("S"),speak("T"),speak("R"),speak("A"),speak("W"),speak("B"),speak("E"),speak("R"),speak("R"),speak("I"),speak("E"),speak("S"),speak("STRAWBERRIES")])
    fb.grid(row=5,column=1,padx=10,pady=5,ipadx=3)
    
    my_label=Label(root2,image=newimg7)
    my_label.grid(row=6,column=0)
    fb=Button(root2,text="PINEAPPLE",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("P"),speak("I"),speak("N"),speak("E"),speak("A"),speak("P"),speak("P"),speak("L"),speak("E"),speak("PINEAPPLE")])
    fb.grid(row=7,column=0,padx=10,pady=5,ipadx=22)

    my_label=Label(root2,image=newimg8)
    my_label.grid(row=6,column=1)
    fb=Button(root2,text="GRAPES",bg='#5b437d',fg='#ffffff',font=("Helvetica",12,'bold'),command=lambda: [speak("G"),speak("R"),speak("A"),speak("P"),speak("E"),speak("S"),speak("GRAPES")])
    fb.grid(row=7,column=1,padx=10,pady=5,ipadx=35)

    root2.mainloop()
    
fruits()