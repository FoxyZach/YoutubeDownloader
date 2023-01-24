from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Completed!')

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='D:\Python\PythonScripts\Projects\yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 55, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))
link_description1 = Label(screen, text="Program May Freeze While Downloading!", font=('Arial', 10))
link_description2 = Label(screen, text="Longer Video Duration = Longer Downloading Time", font=('Arial', 10))
link_creds = Label(screen, text="Made By Zach", font=('Arial', 10))
link_github = Label(screen, text="https://github.com/FoxyZach", font=('Arial', 10))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 183, window=link_description2)
canvas.create_window(250, 160, window=link_description1)
canvas.create_window(250, 135, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(8, 475, window=link_creds)
canvas.create_window(88, 494, window=link_github)

#Download btns
download_btn = Button(screen, text="Download Video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()