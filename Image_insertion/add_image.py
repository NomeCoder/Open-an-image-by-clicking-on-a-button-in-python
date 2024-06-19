import tkinter as tk
from tkinter import Label
from tkinter import Toplevel
from PIL import Image, ImageTk

def pic_window ():

    
    mypic=Toplevel(root)
    mypic.geometry("300x200") #defining the child image
    mypic.title("Tiger image")

    image_path="C:/Users/Administrator/Desktop/Image_insertion/Tiger.jpg"
    openimage=Image.open(image_path) #opening the child image


    image=ImageTk.PhotoImage(openimage)
    #importing child image in tkinter

    label=Label(mypic, image=image)
    label.image = image
    label.pack() #labeling the child image inside tkinter(important)



def pic_window1():
    myimg=Toplevel(root)
    myimg.title("Mounatin")
    myimg.geometry("266x200")

    image_path1="C:/Users/Administrator/Desktop/Image_insertion/Mountain.jpg"
    openimage1=Image.open(image_path1)
    imgtki=ImageTk.PhotoImage(openimage1)

    label1=Label(myimg, image=imgtki)
    label1.image=imgtki
    label1.pack()


root=tk.Tk()
root.geometry("300x300")
root.title("CLICK HERE!")

lbl= Label(root, text="What do you want to see ?")
lbl.pack()

button=tk.Button(root,text="Click to see tiger !", command=pic_window)
button.pack()
button1=tk.Button(root, text="click to see mountain!", command=pic_window1)
button1.pack()



root.mainloop()