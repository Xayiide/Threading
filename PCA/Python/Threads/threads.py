import threading
import time



def enumerateThreads():
    print("Enumeration of threads:")
    for i in threading.enumerate():
        print(" ·", i.getName())

def numberOfThreads():
    print("Number of threads: " + str(threading.active_count()))

def currentThreadName():
    print("Current thread name: " + threading.current_thread().getName())






def function():
    print("I'm thread", currentThreadName())
    print(currentThreadName(), enumerateThreads())
    print(currentThreadName(), "completed.")


def main():
    numberOfThreads()
    currentThreadName()
    enumerateThreads()
    
    t1 = threading.Thread(name="t1", target=function)
    print("[M] Starting", t1.getName())
    t1.start()
    
    print("[M] Joining", t1.getName())
    t1.join()
    print("Main complete!")






#print("dir: " + str(dir(threading.current_thread())))
#print("dir: " + str(dir(threading.enumerate())))

if __name__ == '__main__':
    main()

