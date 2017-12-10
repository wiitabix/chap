import os

def run(*args):
    print("{} passed into environment module.".format(*args))
    return str(os.environ)
