
# Thread:
# if we break down a big task into smaller parts each part is called a thread
# by defualt every exicution ha one thread i.e.,'main thread'
# if two threads are coming at the cpu at a time then it call "collision"




from threading import *

from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)

t1=Hello()
t2=Hi()
t1.start()
sleep(0.2)                        #it means print t1 after 0.2 seconds print t2
t2.start()

#if we wnat to print bye at last line

#print('bye')                  # bye come  in  3rd line. to overcome this problem we use join()

# join():after t1 and t2 join then only bye comes into picture
t1.join()
t2.join()
print('bye')





