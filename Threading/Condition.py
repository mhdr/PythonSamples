# represents the addition of an item to a resource
import threading

condition = threading.Condition()

# producer thread
# generate item
condition.acquire()
# add item to resource
condition.notify() # signal that a new item is available
condition.release()