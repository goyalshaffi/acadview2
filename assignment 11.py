# q1
'''
import threading
import time
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass
    def run(self):
        time.sleep(5)
        print("the value will print after 5 sec")

thread1=Mythread()
thread1.start()


# q2

import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(1)
        print("no is:",self.h)
for i in range(1,11):
    thread1=Mythread(i)
    thread1.start()


# q3

l=[56,99,57,45,67]
import threading
import time
class Mythread(threading.Thread):
        def __init__(self):
           threading.Thread.__init__(self)
        pass
        def run(self):
            count=0
            while(count<12):
                time.sleep(2*count)
                print(i)
for i in l():
    thread1=Mythread(i)
    thread1.start()

'''

# q4

n=int("enter value")
import threading
import math
class Mythread(threading.thread):
    def __init__(self):
        threading.Thread.__init__(self,n)
        self.N=n
    def run(self):
        print(self.a,math.factorial(self.a)))
g=Mythread()
g.start()


