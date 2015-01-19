__author__ = 'mahmood'

from concurrent.futures import ThreadPoolExecutor

thread_pool=ThreadPoolExecutor(5)

def print_msg(msg,callback):
    print(msg)
    result="end of msg : {0}".format(msg)
    callback(result)


def do_callback(msg):
    print(msg)

for i in range(1,1000):
    thread_pool.submit(print_msg,i,do_callback)