from tkinter import *
from PIL import ImageTk, Image
from Admin_page import *
from User_page import *

root = Tk()
root.title("Login Page")
root.geometry("1200x720")

# Background image defining
bg = ImageTk.PhotoImage(file=r"C:\Users\maxso\PycharmProjects\DBMS_music-management\colorful_mountains_4K.png")
Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
Label(root, text="LOGIN PAGE")

# page title
Label(root, text="WELCOME TO PHILHARMONIC MUSIC APP", font=("Ariel", 20, "bold"), fg="#FC46AA", padx=20, pady=20).place(
    x=280, y=180)

# defining frame for admin login
frame_1 = Frame(root, padx=20, pady=20)
frame_1.place(x=80, y=400, height=250, width=450)

# widgets inside frame_1
Label(frame_1, text="ADMIN", font=("Comic Sans", 30, "bold"), fg="#FC46AA").place(x=120, y=20)
Label(frame_1, text="Username: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=100)
Label(frame_1, text="Password: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=140)

# write blocks
admin_name = Entry(frame_1, font=("ariel", 14), bg="lightgray").place(x=130, y=105)
admin_psw = Entry(frame_1, font=("ariel", 14), bg="lightgray").place(x=130, y=145)

# defining frame for user login
frame_2 = Frame(root, padx=20, pady=20)
frame_2.place(x=640, y=400, height=250, width=450)

# widgets for frame 2
Label(frame_2, text="USER", font=("Comic Sans", 30, "bold"), fg="#FC46AA").place(x=140, y=20)
Label(frame_2, text="Username: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=100)
Label(frame_2, text="Password: ", font=("Comic Sans", 16, "italic"), fg="#FC46AA").place(x=20, y=140)

# write blocks
usr_name = Entry(frame_2, font=("ariel", 14), bg="lightgray").place(x=130, y=105)
usr_psw = Entry(frame_2, font=("ariel", 14), bg="lightgray").place(x=130, y=145)


# function for opening admin page
def login_admin():
        admin()


def login_usr():
    user()


# login button
Button(frame_1, text="LOGIN", fg="#FC46AA", font=("times new roman", 18), command=login_admin).place(x=160, y=180)
Button(frame_2, text="LOGIN", fg="#FC46AA", font=("times new roman", 18), command=login_usr).place(x=160, y=180)

root.mainloop()
