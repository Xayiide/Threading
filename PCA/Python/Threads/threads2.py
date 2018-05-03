import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s')



def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')



t = threading.Thread(name='myService', target=my_service)
w = threading.Thread(name='worker', target=worker)
y = threading.Thread(target=worker)

w.start()
y.start()
t.start()




print("Exiting!")
exit(12)
# The program will wait to exit until all threads have completed their work
