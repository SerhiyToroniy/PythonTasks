class MyIterator:
    def __init__(self, limit): #limit is upper border for our object(int)
        self.limit = int(limit)
        self.counter = 0

    def __iter__(self): #return our iterator
        return self

    def __next__(self): #return next iterator
        if self.counter < self.limit:   return self.counter
        else:   raise StopIteration

def kaprekars_nums(): #the main function
    n = int(input("Input N: "))
    while n < 1:
        n = int(input("N must be a natural number: "))
    print(1)  # exception
    i = MyIterator(n)  # iterator
    count = 1  # counre for first Kaprekar's nums
    while True:
        if count == n:  return
        P = str(i.counter * i.counter)
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
            int_a = int(a)  # str -> int
            int_b = int(b)
            if int_a + int_b == i.counter and int_a != 0 and int_b != 0:
                print(i.counter)
                count += 1
            b = ""  # update right part
        i.counter += 1
