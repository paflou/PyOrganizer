import os

extensions = (".txt", ".pdf", ".docx", ".doc", ".odt", ".xls", ".xlsx", ".ppt", "pptx", \
    ".m4a", ".mp3", ".flac", ".wav", ".wma", ".aac", \
    ".mp4",".mov", ".avi", ".wmv", ".webm", \
    ".jpg", ".gif", ".png", ".tiff", ".bmp", ".psd", ".raw", ".heif", \
    ".zip", ".7z", ".rar")

for extension in extensions:
    filename = "test" + extension
    open(filename, "w")

os.mkdir("test")