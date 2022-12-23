from tkinter import*
from tkinter import messagebox

from PIL import ImageTk
class welcome:
    def __init__(self,root): #everytime obj is created within class init is called
        self.root=root
        self.root.title("MUSIC MANAGEMENT SYSTEM")
        self.root.geometry("1200x720+400+150")
        #Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\maxso\PycharmProjects\DBMS_music-management\lo-fi-24.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root)
        Frame_login.place(x=280,y=10,height=50,width=620)
        title=Label(Frame_login,text="WELCOME TO MUSIC MANAGEMENT SYSTEM",font=("Ariel",20,"bold"),fg="#FC46AA").place(x=0,y=0)
        Frame_welcome = Frame(self.root)
        Frame_welcome.place(x=450, y=250, height=140, width=253)
        add=Button(Frame_welcome,text="          Add Track            ", fg="#FC46AA", font=("times new roman", 18)).place(x=0, y=0)
        view=Button(Frame_welcome,text="         View Tracks          ",fg="#FC46AA",font=("times new roman",18)).place(x=0,y=47)
        delete=Button(Frame_welcome,text="       Delete Tracks          ", fg="#FC46AA", font=("times new roman", 18)).place(x=0,y=94)


root = Tk()
obj = welcome(root)
root.mainloop()
