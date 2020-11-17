from LinkedList import*
from Validation import*
import random #for generating random nums
import copy

def find_demical(binary):
    i = x = 1
    if int(binary) == 0:#exceprion
        print(0)
        return
    while True:
        bina = ""
        while x != 0:
            b = x % 2
            bina += str(b)
            x //= 2
        bina = bina[::-1]
        if int(bina) == int(binary):#to ignore "0" in the begining of each num
            return i #return decimal num
        i += 1
        x = i#updating x

def create_z(x, y, N):
    z = LinkedList()
    i = 0 #iterator to compare lists
    while i < N:#create z according to the task
        if x[i] > y[i]: z.append(1)
        else:   z.append(0)
        i += 1
    print("X: ")
    x.display()
    print("Y: ")
    y.display()
    print("Z: ")
    z.display()
    while x.length()!=0:
        x.erase(x.length()-1)
    for i in range(z.length()):
        x.append(z[i])
    binary = ""
    for u in range(z.length()):
        binary+=str(z[u])
    return find_demical(binary)#call function to find out a decimal num

def input_with_N(lst):
    v = Validation()
    y = LinkedList()
    N = lst.length()
    start = input("START:")
    while not v.positive_check(start):
        start = input("Start must be a number: ")
    invalid = True
    while invalid:
        for z in start:
            invalid = False
            if z == ".":
                invalid = True
                start = input("Start must be an integer:")
                while not v.positive_check(start):
                    start = input("Start must be a number: ")
                break
    start = int(start)
    end = input("END:")
    while not v.positive_check(end):
        end = input("End must be a number: ")
    invalid = True
    while invalid:
        for z in end:
            invalid = False
            if z == ".":
                invalid = True
                end = input("End must be an integer:")
                while not v.positive_check(end):
                    end = input("End must be a number: ")
                break
    end = int(end)
    for j in range(N):#generate nums for "y"
        y.append(random.randint(start,end))
    result = create_z(lst, y, N)
    return result

def input_without_N(lst):
    x = lst
    v = Validation()
    y = LinkedList()
    first_iter = True
    while x.length()!= y.length():
        if not first_iter:
            print("Both length must be equal!")
        print("Input Y(double ENTER to stop): ")
        while True:  # while user will not input "ENTER", he enters a list
            i = input()
            if i == "":
                break
            if not v.positive_check(i):
                print(i, "was skipped because it's not a number!")
            else:
                dot = False
                for z in i:
                    if z == ".":
                        dot = True
                        break
                if dot:
                    y.append(float(i))
                else:
                    y.append(int(i))
        first_iter = False
    result = create_z(x, y, x.length())#call a function to create list "z" according to task
    return result

def user_choice(lst):
    result = None
    while True:
        choice = input("Input \"1\" for generating list or input \"2\" to create your own list(input smth else to quit): ")#user inputs his own choice how to create lists
        if choice == "1":#user inputs only size
            result = input_with_N(lst)
            print(result)
        if choice == "2":#user inputs only lists
            result = input_without_N(lst)
            print(result)
        if choice != "1" and choice != "2":#user can quit main menu
            return result