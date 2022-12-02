from tkinter import *
from PIL import ImageTk, Image

def user():
    root = Toplevel()
    root.title("USER PAGE")
    root.geometry("1000x667")

    # Backgroung Image
    bg = ImageTk.PhotoImage(file=r"C:\Users\maxso\PycharmProjects\DBMS_music-management\user_2.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # View playlists button
    Button(root, text="VIEW PLAYLISTS", font=("Comic Sans", 35, "bold"), fg="#6F4E37").place(x=300, y=230)
    # Create PLaylist button
    Button(root, text="CREATE PLAYLIST", font=("Comic Sans", 35, "bold"), fg="#6F4E37").place(x=280, y=450)



    root.mainloop()


