from threading import Thread
from time import sleep

class NewThread(Thread):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def run(self):
        sleep(1)
        print("printing from another thread")

        self.new_value = self.value + 2



th = NewThread(3)
th.start()
print("from main thread")

th.join()

print(th.new_value)