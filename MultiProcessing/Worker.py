import time

__author__ = 'mahmood'

import multiprocessing

def my_sum(data):
    x=data[0]
    y=data[1]
    return x+y

num_of_workers=multiprocessing.cpu_count()
pool=multiprocessing.Pool(num_of_workers)

data=[]

print("Start generation : {0}".format(time.asctime( time.localtime(time.time()) )))

for i in range(1,100000000):
    data.append((1,1))

print("End of generation : {0}".format(time.asctime( time.localtime(time.time()) )))

print("Start calculation : {0}".format(time.asctime( time.localtime(time.time()) )))

pool.map(my_sum,data)

print("End of calculation : {0}".format(time.asctime( time.localtime(time.time()) )))