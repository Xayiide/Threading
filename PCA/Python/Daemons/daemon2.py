import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s')


def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)


d.start()
t.start()


d.join() # Waits until the daemon thread has completed its work. By default, join() waits indefinitely
# d.join(1) # Means: wait 1 second for the daemon-thread "d" to finish. If the thread does not complete
# its work in 1 second, join return anyway

print("Main completed!")
exit(12)
