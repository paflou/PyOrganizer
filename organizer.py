import glob
import shutil
import os
import tkinter as tk
from tkinter import filedialog
import sys

def browse():
    path = filedialog.askdirectory()
    global folder_path
    if path:
        folder_path = path
        print("Selected Folder: ", path)
        label = tk.Label(root, text = path)
        label.pack()

def begin():
    files = glob.glob(folder_path + "/*")
    print(files)
    for file in files:
        file = os.path.relpath(file, folder_path)
        #document file formats
        if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") \
        or file.endswith(".doc") or file.endswith(".odt") or file.endswith(".xls") \
        or file.endswith(".xlsx") or file.endswith(".ppt") or file.endswith(".pptx"):
            organize(file, "documents")

        #audio file formats
        elif file.endswith(".m4a") or file.endswith(".mp3") or file.endswith(".flac") \
        or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".aac"):
            organize(file,"audio")

        #video file formats
        elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi") \
        or file.endswith(".wmv") or file.endswith(".webm"):
            organize(file,"videos")

        #image file formats
        elif file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".png") \
        or file.endswith(".tiff") or file.endswith(".bmp") or file.endswith(".psd") \
        or file.endswith(".raw") or file.endswith(".heif"):
            organize(file,"images")

        #archive file formats
        elif file.endswith(".zip") or file.endswith(".7z") or file.endswith(".rar") \
        or ".tar" in file:
            organize(file,"archives")

        elif "." not in file and file != "":
            folders(file)

        #everything else
        else:
            if file == "organizer.py" or  "." not in file:
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