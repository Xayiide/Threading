import threading
import time
import os

def timer(name, delay, repeat):
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + "Timing!")
        repeat -= 1
    print("Timer: " + name + "completed")

def printer(name, delay, repeat):
    while repeat > 0:
        time.sleep(delay)
        print("Hello I'm " + name + "and printing!")
        repeat -= 1
    print("Printer: " + name + "completed")

def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=printer, args=("Printer1", 5, 2))
    t1.start()
    t2.start()
    
    repeat = 10
    while repeat > 0:
        print("Number of threads: " + str(threading.active_count()))
        repeat -= 1
        time.sleep(1)

    print("Main Completed")

if __name__ == '__main__':
    Main()
