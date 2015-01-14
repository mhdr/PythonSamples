__author__ = 'mahmood'

import threading

def print_msg(thread_name,msg,callback:"function"):
    print("Thread Name : {0} , Msg : {1}".format(thread_name,msg))
    result="thread name : {0} - result : {1}".format(thread_name,1)
    error=0
    callback(result,error)

def print_callback(result,error):
    print("result : {0}".format(result))
    print("error : {0}".format(error))


threading.Thread(target=print_msg,args=("thread1","Mahmood",print_callback)).start()
threading.Thread(target=print_msg,args=("thread2","Javad",print_callback)).start()