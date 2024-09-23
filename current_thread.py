
import threading
from time import sleep

def task(value: int):
    sleep(value)
    print(f"current Thread, {threading.current_thread()}")

    

threading.Thread(target=task, args=(2,)).start()
threading.Thread(target=task, args=(1,)).start()