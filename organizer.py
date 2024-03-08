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

        elif "." not in file:
            folders(file)

        #everything else
        else:
            if file == "organizer.py" or  "." not in file:
                continue
            print("Moving "+ file + " to misc folder")
            misc(file)


def documents(file):
    if(not os.path.exists(os.getcwd() + "/documents")):
        os.mkdir("documents")
    print("Moving "+ file + " to document folder")
    shutil.move(file,"documents/" + file)

def audio(file):
    if(not os.path.exists(os.getcwd() + "/audio")):
        os.mkdir("audio")
    print("Moving " + file +" to audio folder")
    shutil.move(file,"audio/" + file)

def videos(file):
    if(not os.path.exists(os.getcwd() + "/videos")):
        os.mkdir("videos")
    print("Moving "+ file + " to videos folder")
    shutil.move(file,"videos/" + file)

def images(file):
    if(not os.path.exists(os.getcwd() + "/images")):
        os.mkdir("images")
    print("Moving "+ file + " to images folder")
    shutil.move(file,"images/" + file)

def archives(file):
    if(not os.path.exists(os.getcwd() + "/archives")):
        os.mkdir("archives")
    print("Moving "+ file + " to archives folder")
    shutil.move(file,"archives/" + file)

def folders(file):
    if(not os.path.exists(os.getcwd() + "/folders")):
        os.mkdir("folders")
        
    #dont put your folders
    if not(file == "documents" or file == "audio" or file == "videos" \
    or file == "images" or file == "archives" or file =="misc" or file == "folders"):
        print("Moving "+ file + " to folders folder")
        shutil.move(file,"folders/" + file)

def misc(file):
    if(not os.path.exists(os.getcwd() + "/misc")):
        os.mkdir("misc")
    shutil.move(file,"misc/" + file)

organize()