import glob
import shutil
import os
import tkinter as tk
from tkinter import filedialog
import sys

folder_path = ""

def browse():
    global folder_path  # Declare folder_path as global
    path = filedialog.askdirectory()
    if path:
        folder_path = path
        print("Selected Folder: ", path)
        label = tk.Label(root, text = path)
        label.pack()

def begin():
    global folder_path  # Declare folder_path as global
    if folder_path== "":
        folder_path = os.getcwd()
    
    files = glob.glob(folder_path + "/*")
    print(files)
    for file in files:
        file = os.path.relpath(file, folder_path)

        documents = (".txt", ".pdf", ".docx", ".doc", ".odt", ".xls", ".xlsx", ".ppt", "pptx")
        audio = (".m4a", ".mp3", ".flac", ".wav", ".wma", ".aac")
        video = (".mp4",".mov", ".avi", ".wmv", ".webm")
        audio = (".jpg", ".gif", ".png", ".tiff", ".bmp", ".psd", ".raw", ".heif")
        archive = (".zip", ".7z", ".rar")

        if file.endswith(documents):
            organize(file, "documents")

        #audio file formats
        elif file.endswith(audio):
            organize(file,"audio")

        #video file formats
        elif file.endswith(video):
            organize(file,"videos")

        #image file formats
        elif file.endswith(audio):
            organize(file,"images")

        #archive file formats
        elif file.endswith(archive) or ".tar" in file:
            organize(file,"archives")

        elif "." not in file and file != "":
            folders(file)

        #everything else
        else:
            if file == "organizer.py" or file == "createTests.py" or  "." not in file:
                continue
            organize(file,"misc")

    successMessage = "Complete!"
    print(successMessage)


def organize(file, type):
    if(not os.path.exists(folder_path + "/" + type)):
        os.mkdir(folder_path + "/" + type)
    movingMessage = "Moving "+ file + " to " + type +" folder"
    print(movingMessage)
    shutil.move(folder_path + "/" + file,folder_path +"/" + type + "/" + file)

def folders(file):
    #dont put your folders
    if not(file == "documents" or file == "audio" or file == "videos" \
    or file == "images" or file == "archives" or file =="misc" or file == "folders"):
        if(not os.path.exists(folder_path + "/folders")):
            os.mkdir(folder_path + "/folders")
        movingMessage = "Moving "+ file + " to folders folder"
        print(movingMessage)
        shutil.move(folder_path + "/" + file,folder_path +"/folders/" + file)

# Start the main event loop
if(len(sys.argv) > 1):

    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("400x200")

    browse_button = tk.Button(root, text="Browse", command=browse)
    browse_button.pack(side="right",anchor="s")

    run_button = tk.Button(root, text="Start", command=begin, bg="green")
    run_button.pack(side="left", anchor="s")
    root.mainloop()
else:
    folder_path = input("Select the directory you wish to organize : \n")
    if folder_path == "":
        folder_path = os.getcwd()
    begin()