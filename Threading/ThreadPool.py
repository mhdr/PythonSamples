__author__ = 'mahmood'

from concurrent.futures import ThreadPoolExecutor

thread_pool=ThreadPoolExecutor(5)

def print_msg(msg):
    print(msg)


for i in range(1,1000):
    thread_pool.submit(print_msg,i)