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


print("Main completed!")
exit(12)
# The exiting message from the daemon is not sent, as every other thread is done before the daemon
# awakes from its 2 second sleep.
