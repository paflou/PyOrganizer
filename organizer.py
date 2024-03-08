import glob

def organize():
    files = glob.glob('*')
    for file in files:
        if file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".docx") \
        or file.endswith(".doc") or file.endswith(".odt"):
            print("Moving "+ file + " to text folder")
        elif file.endswith(".") or file.endswith(".mp3")

organize()