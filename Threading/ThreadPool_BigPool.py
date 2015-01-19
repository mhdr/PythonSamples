from concurrent.futures import ThreadPoolExecutor

# thread_pool=ThreadPoolExecutor(1)
thread_pool=ThreadPoolExecutor(500)

def print_msg(msg):
    print(msg)


for i in range(1,1000000):
    thread_pool.submit(print_msg,i)