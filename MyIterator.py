class MyIterator:
    def __init__(self, limit): #limit is upper border for our object(int)
        self.limit = int(limit)
        self.counter = 0

    def __iter__(self): #return our iterator
        return self

    def __next__(self): #return next iterator
        while self.limit > 0:
            if self.counter == 1:
                self.counter+=1
                self.limit-=1
                return self.counter-1
            P = str(self.counter * self.counter)
            a = b = ""  # a - left part / b - right part
            z = k = 1  # z ignore left part for correct creatting right part / k remember left part's len
            for j in P:
                a += j  # add symbols from right to left
                if a == P:  continue
                for h in P:
                    if z > 0:  # z is used for the independece of k
                        z -= 1
                        continue
                    b += h
                k += 1
                z = k
                if int(a) + int(b) == self.counter and int(a) != 0 and int(b) != 0:
                    self.limit -= 1
                    self.counter+=1
                    return self.counter-1
                b = ""
            self.counter += 1
        raise StopIteration

def validate():
    count = int(input("Input N: "))
    while count < 1: count = int(input("N must be a natural number: "))
    for i in MyIterator(count):
        print(i)
