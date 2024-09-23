# import threading
# from time import sleep

# def task(value: int):
#     local = threading.local()
#     local.value = value
#     sleep(value)
#     print(f'Stored value: {local.value}')


# threading.Thread(target=task, args=(2, )).start()
# threading.Thread(target=task, args=(1, )).start()



#Sharing Thread local value
import threading
from time import sleep

def task(value: int, local):
    local.value = value
    sleep(value)
    print(f"Local Value: {local.value}")
    

local = threading.local()
threading.Thread(target=task, args=(2, local)).start()
threading.Thread(target=task, args=(1, local)).start()
