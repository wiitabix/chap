import os

def run(*args):
    print("{} passed into dirlister module.".format(*args))
    files = os.listdir(".")

    return str(files)
    
