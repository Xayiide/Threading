import threading
import time
import inspect


count = 0
lock = threading.Lock()

def incre():
    global count
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print("Inside %s()" % caller)
    print("Acquiring lock")
    with lock:
        print("Lock acquired")
        count += 1
        print("Count:", count)
        time.sleep(2)

def bye():
    while count < 5:
        incre()

def hello_there():
    while count < 5:
        incre()



def main():
    hello = threading.Thread(target=hello_there)
    hello.start()
    goodbye = threading.Thread(target=bye)
    goodbye.start()
    


if __name__ == '__main__':
    main()
