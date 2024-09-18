
import threading

from time import sleep

class ThreadingStart(threading.Thread):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def run(self):
        sleep(1)
        print(f"running from another thread. Value from initializer: {self.value}")


th = ThreadingStart(4)
th.start()
print("waiting for the thread response")
th.join()
