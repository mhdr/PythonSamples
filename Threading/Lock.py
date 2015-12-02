import threading
from threading import Lock

def print_multi():
    lock=Lock()

    lock.acquire()

    print("Hello World")

    lock.release()





print_multi()