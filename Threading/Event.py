import threading

event = threading.Event()

# a client thread can wait for the flag to be set
event.wait()

# a server thread can set or reset it
event.set()

# when the event is cleared it waits
event.clear()