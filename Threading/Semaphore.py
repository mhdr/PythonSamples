import threading

semaphore = threading.BoundedSemaphore(10)
semaphore.acquire() # decrements the counter
# access the shared resource
semaphore.release() # increments the counter