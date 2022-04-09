from tkinter import *
from tkvideo import tkvideo
from tts import speak
from PIL import Image,ImageTk

root=Tk()

myimg1=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/apple.jpg")
myimg2=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/bananas.jpg")
myimg3=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/guava.jpg")
myimg4=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/orange.jpg")
myimg5=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/kiwi.jpg")
myimg6=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/strawberries.jpg")
myimg7=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/pineapple.jpg")
myimg8=Image.open("C:/Users/DELL/Documents/VS/HACKATHONS/EDLEXIC/fruitimages/grape.jpg")

resize1=myimg1.resize((180,160),Image.ANTIALIAS)
resize2=myimg2.resize((180,160),Image.ANTIALIAS)
resize3=myimg3.resize((180,160),Image.ANTIALIAS)
resize4=myimg4.resize((180,160),Image.ANTIALIAS)
resize5=myimg5.resize((180,160),Image.ANTIALIAS)
resize6=myimg6.resize((180,160),Image.ANTIALIAS)
resize7=myimg7.resize((180,160),Image.ANTIALIAS)
resize8=myimg8.resize((180,160),Image.ANTIALIAS)

newimg1=ImageTk.PhotoImage(resize1)
newimg2=ImageTk.PhotoImage(resize2)
newimg3=ImageTk.PhotoImage(resize3)
newimg4=ImageTk.PhotoImage(resize4)
newimg5=ImageTk.PhotoImage(resize5)
newimg6=ImageTk.PhotoImage(resize6)
newimg7=ImageTk.PhotoImage(resize7)
newimg8=ImageTk.PhotoImage(resize8)



my_label=Label(root,image=newimg1)
my_label.grid(row=0,column=0)
my_label=Label(root,image=newimg2)
my_label.grid(row=0,column=1)
my_label=Label(root,image=newimg3)
my_label.grid(row=1,column=0)
my_label=Label(root,image=newimg4)
my_label.grid(row=1,column=1)
my_label=Label(root,image=newimg5)
my_label.grid(row=2,column=0)
my_label=Label(root,image=newimg6)
my_label.grid(row=2,column=1)
my_label=Label(root,image=newimg7)
my_label.grid(row=3,column=0)
my_label=Label(root,image=newimg8)
my_label.grid(row=3,column=1)

root.mainloop()