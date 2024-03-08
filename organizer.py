import glob
import shutil
import os
import tkinter as tk
from tkinter import filedialog

def browse():
    path = filedialog.askdirectory()
    if path:
        FOLDER_PATH = path
        print("Selected Folder: ", path)
        label = tk.Label(root, text = path)
        label.pack()

def organize():
    files = glob.glob(FOLDER_PATH + "/*")
    print(files)
    for file in files:
        file = os.path.relpath(file, FOLDER_PATH)
        #document file formats
        if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") \
        or file.endswith(".doc") or file.endswith(".odt") or file.endswith(".xls") \
        or file.endswith(".xlsx") or file.endswith(".ppt") or file.endswith(".pptx"):
            documents(file)

        #audio file formats
        elif file.endswith(".m4a") or file.endswith(".mp3") or file.endswith(".flac") \
        or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".aac"):
            audio(file)

        #video file formats
        elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi") \
        or file.endswith(".wmv") or file.endswith(".webm"):
            videos(file)

        #image file formats
        elif file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".png") \
        or file.endswith(".tiff") or file.endswith(".bmp") or file.endswith(".psd") \
        or file.endswith(".raw") or file.endswith(".heif"):
            images(file)

        #archive file formats
        elif file.endswith(".zip") or file.endswith(".7z") or file.endswith(".rar") \
        or ".tar" in file:
            archives(file)

        elif "." not in file and file != "":
            folders(file)

        #everything else
        else:
            if file == "organizer.py" or  "." not in file:
                continue
            misc(file)

    successMessage = "Complete!"
    print(successMessage)
    label = tk.Label(root, text = successMessage)
    label.pack()


def documents(file):
    if(not os.path.exists(FOLDER_PATH + "/documents")):
        os.mkdir(FOLDER_PATH + "/documents")
    movingMessage = "Moving "+ file + " to documents folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/documents/" + file)

def audio(file):
    if(not os.path.exists(FOLDER_PATH + "/audio")):
        os.mkdir(FOLDER_PATH + "/audio")
    movingMessage = "Moving "+ file + " to audio folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()    
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/audio/" + file)

def videos(file):
    if(not os.path.exists(FOLDER_PATH + "/videos")):
        os.mkdir(FOLDER_PATH + "/videos")
    movingMessage = "Moving "+ file + " to videos folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()    
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/videos/" + file)

def images(file):
    if(not os.path.exists(FOLDER_PATH + "/images")):
        os.mkdir(FOLDER_PATH + "/images")
    movingMessage = "Moving "+ file + " to images folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()    
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/images/" + file)

def archives(file):
    if(not os.path.exists(FOLDER_PATH + "/archives")):
        os.mkdir(FOLDER_PATH + "/archives")
    movingMessage = "Moving "+ file + " to archives folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()    
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/archives/" + file)

def folders(file):
    if(not os.path.exists(FOLDER_PATH + "/folders")):
        os.mkdir(FOLDER_PATH + "/folders")
    #dont put your folders
    if not(file == "documents" or file == "audio" or file == "videos" \
    or file == "images" or file == "archives" or file =="misc" or file == "folders"):
        movingMessage = "Moving "+ file + " to folders folder"
        print(movingMessage)
        label = tk.Label(root, text = movingMessage)
        label.pack()    
        shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/folders/" + file)

def misc(file):
    if(not os.path.exists(FOLDER_PATH + "/misc")):
        os.mkdir(FOLDER_PATH + "/misc")
    movingMessage = "Moving "+ file + " to misc folder"
    print(movingMessage)
    label = tk.Label(root, text = movingMessage)
    label.pack()
    shutil.move(FOLDER_PATH + "/" + file,FOLDER_PATH +"/misc/" + file)

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

browse_button = tk.Button(root, text="Browse", command=browse)
browse_button.pack(side="right",anchor="s")

run_button = tk.Button(root, text="Start", command=organize, bg="green")
run_button.pack(side="left", anchor="s")

global FOLDER_PATH
FOLDER_PATH = os.getcwd()
# Start the main event loop
root.mainloop()