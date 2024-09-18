import threading

from time import sleep

class ThreadingStart(threading.Thread):

    def run(self):
        sleep(1)
        print("running from another thread")


th = ThreadingStart()
th.start()
print("waiting for the thread response")
th.join()
