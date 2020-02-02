import threading
import time
class ak(threading.Thread):
    def run(self):
        for i in range(10):
            print("dsl")
            time.sleep(1)

class am(threading.Thread):
    def run(self):
        for i in range(10):
            print ("dave")
            time.sleep(1)

t1=ak()
t2=am()
t1.start()
t2.start()
t1.join()
t2.join()