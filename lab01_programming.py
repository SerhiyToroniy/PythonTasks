def k_nums(n):
     print (1) #exception
     i = 1 #iterator
     count = 1 # counre for first Kaprekar's nums
     while True:
          if count == n:
               return
          my_pow = i * i
          P = str(my_pow)
          a = b ="" #a - left part / b - right part
          z = k = 1 #z ignore left part for correct creatting right part / k remember left part's len
          for j in P:
               a += j #add symbols from right to left
               if a == P:
                    continue
               for h in P:
                    if z > 0: #z is used for the independece of k
                         z -= 1
                         continue
                    b += h
               k += 1
               z = k
               int_a = int(a) #str -> int
               int_b = int(b)
               if int_a + int_b == i and int_a != 0 and int_b != 0:
                         print(i)
                         count += 1
               b = "" #update right part
          i += 1
def validation():
     check = False
     while not check:
          temp = int(input("Input N: "))
          check = True
          if temp <= 0:
               check = False
               print("N must be natural!")
     k_nums(temp)
validation()
