__author__ = 'Mahmood'

import threading

def print_msg(thread_name,msg):
    print("Thread Name : {0} , Msg : {1}".format(thread_name,msg))


threading.Thread(target=print_msg,args=("thread1","Mahmood")).start()
threading.Thread(target=print_msg,args=("thread2","Javad")).start()