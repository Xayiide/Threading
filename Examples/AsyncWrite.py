import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
        print("AsyncWrite created!")

    def run(self):
        print("Writing thread running.")
        f = open(self.out, "a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("Finished Background File Write to " + self.out)

def Main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message, 'out.txt')
    print("# of threads: " + str(threading.active_count()))
    print("We're still not Writing anything")
    background.start()
    print("Now we are. Threads: " + str(threading.active_count()))
    print("The program can continue while it writes in another thread")
    print("100 + 400 = ", 100+400)
    print("Now we join.")
    background.join() # Wait until the thread terminates
    print("Threads: " + str(threading.active_coun()))
    # Wait until the bg thread is done and then it will continue
    print("Waited until thread was complete")


if __name__ == '__main__':
    Main()
