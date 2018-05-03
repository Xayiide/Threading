import os
import threading


def f1(name):
    print("I'm Thread", name)
    f.readline()
    print(name, "completed")



def Main():
    f = open("file1", "r")
    t1 = threading.Thread(target=f1, args="t1")
    t2 = threading.Thread(target=f1, args="t2")

    t1.start()
    t2.start()

    print("Main complete")



if __name__ == "__main__":
    Main()
