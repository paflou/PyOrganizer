import glob
import shutil
import os


def organize():
    files = glob.glob('*')
    for file in files:
        #document file formats
        if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") \
        or file.endswith(".doc") or file.endswith(".odt") or file.endswith(".xls") \
        or file.endswith(".xlsx") or file.endswith(".ppt") or file.endswith(".pptx"):
            print("Moving "+ file + " to document folder")
            documents(file)

        #audio file formats
        elif file.endswith(".m4a") or file.endswith(".mp3") or file.endswith(".flac") \
        or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".aac"):
            print("Moving " + file +" to audio folder")
            audio(file)

        #video file formats
        elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi") \
        or file.endswith(".wmv") or file.endswith(".webm"):
            print("Moving "+ file + " to videos folder")
            videos(file)

        #image file formats
        elif file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".png") \
        or file.endswith(".tiff") or file.endswith(".bmp") or file.endswith(".psd") \
        or file.endswith(".raw") or file.endswith(".heif"):
            print("Moving "+ file + " to images folder")
            images(file)

        #everything else
        else:
            if(file == "organizer.py"):
                continue
            print("Moving "+ file + " to misc folder")
            misc(file)


def documents(file):
    if(not os.path.exists(os.getcwd() + "/documents")):
        os.mkdir("documents")
    shutil.move(file,"documents/" + file)

def audio(file):
    if(not os.path.exists(os.getcwd() + "/audio")):
        os.mkdir("audio")
    shutil.move(file,"audio/" + file)

def videos(file):
    if(not os.path.exists(os.getcwd() + "/videos")):
        os.mkdir("videos")
    shutil.move(file,"videos/" + file)

def images(file):
    if(not os.path.exists(os.getcwd() + "/images")):
        os.mkdir("images")
    shutil.move(file,"images/" + file)

def misc(file):
    if(not os.path.exists(os.getcwd() + "/misc")):
        os.mkdir("misc")
    shutil.move(file,"misc/" + file)

organize()