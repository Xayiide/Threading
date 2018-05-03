import threading

cLock = threading.Lock() # A lock for the variable count
count = 0

def add():
    global count
    cLock.acquire() # We take the variable
    count += 1
    print("count:", count)
    cLock.release()

def sub():
    global count
    with cLock:
        count -= 1
        print("count:", count)

t1 = threading.Thread(name="addThread", target=add)
t2 = threading.Thread(name="subthread", target=sub)

t1.start()
t2.start()

print("Main completed!")
exit(1)
