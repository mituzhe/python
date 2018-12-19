import time, random
import threading

def worker():
    print("worker")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target = worker)
        t.start()
        
'''
count = 0
class Counter(threading.Thread):
    def __init__(self, lock, threadName):
        super(Counter, self).__init__(name = threadName)
        self.lock = lock
    def run(self):
        global count
        self.lock.acquire()
        for i in range(1000):
            count = count + 1
        self.lock.release()

lock = threading.Lock()
for i in range(5):
    Counter(lock,'thread--'+str(i)).start()
time.sleep(2)
print(count)
'''
