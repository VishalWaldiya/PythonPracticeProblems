from threading import Thread,Condition

class Numbers:
    def __init__(self):
        self.numb = []
        self.c = Condition()

    def produceNumbers(self, n):
        self.c.acquire()
        for i in range(1,n+1):
            self.numb.append(i)
        self.c.notifyAll()
        self.c.release()

class EvenNumbers:
    def __init__(self,number ):
        self.numbers = number
        self.evenNumbers = []

    def consume(self):
        self.numbers.c.acquire()
        self.numbers.c.wait(timeout=0)
        print("start Consuming")
        for i in self.numbers.numb:
            if not i%2:
                self.evenNumbers.append(i)
        self.numbers.c.release()
        print("Even Numbers are \n")
        for i in self.evenNumbers:
            print(i)

class OddNumbers:
    def __init__(self,number ):
        self.numbers = number
        self.oddNumbers = []

    def consume(self):
        self.numbers.c.acquire()
        self.numbers.c.wait(timeout=0)
        print("start Consuming")
        for i in self.numbers.numb:
            if i%2:
                self.oddNumbers.append(i)
        self.numbers.c.release()
        print("Odd Numbers are \n")
        for i in self.oddNumbers:
            print(i)

numb = Numbers()
evennumber = EvenNumbers(numb)
oddnumbers = OddNumbers(numb)

t1 = Thread(target=numb.produceNumbers,args=(10,))
t2 = Thread(target=evennumber.consume)
t3 = Thread(target=oddnumbers.consume)

t1.start()
t2.start()
t3.start()
