from tkinter import *
from pytube import YouTube

def download_video(event):
    user_input = user_link.get()
    yt = YouTube(str(user_input))
    video = yt.streams.first()
    video.download(filename="videodlllll")
    
root = Tk()

title = Label(root, text="Vid2Dwonload")
title.pack()

user_link = Entry(root)
user_link.pack()

dl_button = Button(root, text="Download MP4", fg="green", bg="yellow")
dl_button.bind("<Button-1>",download_video)
dl_button.pack()

root.mainloop()