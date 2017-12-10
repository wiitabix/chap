import os

def run(*args):
    print("[*] passed into environment module.")
    return str(os.environ)
