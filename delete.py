from tkinter import *
from sqlite3 import *
from PIL import ImageTk, Image
from backend import *

def delete_song():
    global song_name, artist_name

    root = Toplevel()
    root.title("Deleting Song page")
    root.geometry("1000x667")

    bg = ImageTk.PhotoImage(file=r"C:\Users\maxso\PycharmProjects\DBMS_music-management\delete.jpg")
    Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Page title
    Label(root, text="DELETE A SONG FROM RECORD", font=("Ariel", 30, "bold"), padx=20, pady=20, bg="#000000", fg="#FFFFFF").place(x=200, y=180)

    # labels
    Label(root, text="Song Name: ", font=("Comic Sans", 20, "italic"), bg="#000000", fg="#FFFFFF").place(x=300, y=300)
    Label(root, text="Artist Name: ", font=("Comic Sans", 20, "italic"), bg="#000000", fg="#FFFFFF").place(x=300, y=400)

    # Input fields
    song_name = Entry(root, font=("ariel", 20), bg="lightgray").place(x=490, y=300)
    artist_name = Entry(root, font=("ariel", 20), bg="lightgray").place(x=490, y=400)

    # Buttons for submit or quit
    Submit_btn = Button(root, text="SUBMIT", font=("Comic Sans", 25, "bold"), bg="#000000", fg="#FFFFFF").place(x=340, y=500)
    quit_btn = Button(root, text="QUIT", font=("Comic Sans", 25, "bold"), bg="#000000", fg="#FFFFFF", padx=20, command=root.destroy).place(x=600, y=500)

    root.mainloop()


