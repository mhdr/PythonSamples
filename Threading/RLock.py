import threading
from threading import Lock

def print_multi():
    lock = threading.Lock()
    lock.acquire()
    lock.acquire() # this will block

    lock = threading.RLock()
    lock.acquire()
    lock.acquire() # this won't block





print_multi()