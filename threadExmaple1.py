import threading
import timeit

def add(x,y):
    return x+y

print(timeit.timeit("add(10,20);add(5,6);add(5,30)",globals=globals()))

t = threading.Thread(target=add,args=(10,20))
t2 = threading.Thread(target=add,args=(5,6))
t3 = threading.Thread(target=add,args=(5,30))
t.start();t2.start();t3.start()
