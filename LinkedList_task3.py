from LinkedList import*
from Validation import*
import random #for generating random nums

# class node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
#
# class linked_list:
#     def __init__(self):
#         self.head=node()
#
#     def append(self,data):#add data to list
#         new_node=node(data)#create new node with "data"
#         cur=self.head
#         while cur.next is not None:
#             cur=cur.next
#         cur.next=new_node#if list was empty
#
#     def len(self):#return integer value of list's length
#         cur=self.head
#         total=0 #counter
#         while cur.next is not None:
#             total+=1
#             cur=cur.next
#         return total
#
#     def display(self): #the same as print(list)
#         elems=[]
#         cur_node=self.head
#         while cur_node.next is not None:
#             cur_node=cur_node.next
#             elems.append(cur_node.data) #append every node to empty list
#         print(elems) #print list
#
#     def get(self,index): #return data by index
#         if index>=self.len() or index<0: #index is out of range
#                     return None
#         cur_idx=0 #counter
#         cur_node=self.head
#         while True:
#             cur_node=cur_node.next
#             if cur_idx==index: return cur_node.data #we found it
#             cur_idx+=1
#
#     def __getitem__(self,index): #acsess by index (arr[])
#         return self.get(index) #call get method

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
        if x[i] > y[i]: z.append("1")
        else:   z.append("0")
        i += 1
    # if z.length() == 0:#if lengths of lists aren't same, ValueError will be raise
    #     raise ValueError
    print("X: ")
    x.display()
    print("Y: ")
    y.display()
    print("Z: ")
    z.display()
    binary = ""
    for u in range(z.length()):
        binary+=z[u]
    return find_demical(binary)#call function to find out a decimal num

def input_with_N(lst):
    x = lst
    v = Validation()
    # x = linked_list()
    # N = int(input("Input N: "))
    y = LinkedList()
    N = x.length()
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
    # for i in range(N):#generate nums for "x"
    #     x.append(random.randint(a,b))
    for j in range(N):#generate nums for "y"
        y.append(random.randint(start,end))
    result = create_z(x, y, N)
    return result

def input_without_N(lst):
    x = lst
    # x = linked_list()
    # print("Input X(double ENTER to stop): ")
    # while True:#while user will not input "ENTER", he enters a list
    #     temp = input()
    #     if temp == "":
    #         break
    #     x.append(float(temp))
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
    while True:
        choice = input("Input \"1\" for generating list or input \"2\" to create your own list(input smth else to quit): ")#user inputs his own choice how to create lists
        if choice == "1":#user inputs only size
            print(input_with_N(lst))
        if choice == "2":#user inputs only lists
            print(input_without_N(lst))
        if choice != "1" and choice != "2":#user can quit main menu
            return
#
# def validate_start(lst):
#     check = False
#     while not check: #create infinity loop in order to user finally input correct data
#         try:
#             user_choice(lst) #main function
#             check = True
#         except ValueError:
#             check = False
#             print("N must be a natural number!")
#         except (IndexError, TypeError):
#             check = False
#             print("Sizes of lists must be same!")
#         except NameError:
#             check = False
#             print("\"From\" must be lower than \"To\"!")
#     return True