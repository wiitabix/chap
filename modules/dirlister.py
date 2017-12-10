import os

def run(*args):
    print("[*] passed into dirlister module.")
    files = os.listdir(".")

    return str(files)
    
