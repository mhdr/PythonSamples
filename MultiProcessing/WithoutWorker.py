import time

__author__ = 'mahmood'

import multiprocessing

def my_sum(data):
    x=data[0]
    y=data[1]
    return x+y

print("Start calculation : {0}".format(time.asctime( time.localtime(time.time()) )))

for i in range(1,100000000):
    my_sum((1,1))

print("End of calculation : {0}".format(time.asctime( time.localtime(time.time()) )))