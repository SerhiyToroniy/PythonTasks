def k_nums(n):
     print(1) #exception
     i = 0
     count = 0
     while True:
          if count == n:
               return
          my_pow = i * i
          P = str(my_pow)
          a = b =""
          z = k = 1
          for j in P:
               a += j
               if a == P:
                    continue
               for j in P:
                    if z > 0:
                         z -= 1
                         continue
                    b += j
               k += 1
               z = k
               int_a = int(a)
               int_b = int(b)
               if int_a + int_b == i and int_a != 0 and int_b != 0:
                         print(i)
                         count += 1
               b = ""
          i += 1
k_nums(int(input("Input N: ")))