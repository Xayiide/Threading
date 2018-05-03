import threading

def enumerateThreads():
    print("Enumeration of threads:")
    for i in threading.enumerate():
        print(" ·", i.getName(), "\n")


print("Number of threads: " + str(threading.active_count()))
print("Current thread name: " + threading.current_thread().getName())
#print("dir: " + str(dir(threading.current_thread())))
#print("dir: " + str(dir(threading.enumerate())))
enumerateThreads()



