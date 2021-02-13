<<<<<< practice3
import random #for generating random nums

class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class Linked_list:
	def __init__(self):
		self.head=node()

  def append(self,data):#add data to list
		new_node = node(data)#create new node with "data"
		cur = self.head
		while cur.next != None:
			cur=cur.next
		cur.next=new_node#if list was empty

  def len(self):#return integer value of list's length
		cur=self.head
		total=0 #counter
		while cur.next != None:
			total+=1
			cur=cur.next
		return total

	def display(self): #the same as print(list)
		elems=[]
		cur_node=self.head
		while cur_node.next != None:
			cur_node=cur_node.next
			elems.append(cur_node.data) #append every node to empty list
		print(elems) #print list

	def get(self,index): #return data by index
		if index>=self.len() or index<0: #index is out of range
         			return None
		cur_idx=0 #counter
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data #we found it
			cur_idx+=1

	def __getitem__(self,index): #acsess by index (arr[])
		return self.get(index) #call get method

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
    z = linked_list()
    i = 0 #iterator to compare lists
    while i < N:#create z according to the task
        if x[i] > y[i]:
            z.append("1")
        else:
            z.append("0")
        i += 1
    if z.len() == 0:#if lengths of lists aren't same, ValueError will be raise
        raise ValueError
    print("X: ")
    x.display()
    print("Y: ")
    y.display()
    print("Z: ")
    z.display()
    binary = ""

    #list z -> string z:

    for u in range(z.len()):
        binary+=z[u]
    return find_demical(binary)#call function to find out a decimal num

def input_with_N():
    x = linked_list()
    y = linked_list()
    
    N = int(input("Input N: "))
    a = int(input("From: "))
    b = int(input("To: "))
    if a >= b:
        raise NameError
    for i in range(N):#generate nums for "x"
        x.append(random.randint(a,b))
    for j in range(N):#generate nums for "y"
        y.append(random.randint(a,b))
    result = create_z(x, y, N)
    return result

def input_without_N():
    x = linked_list()
    print("Input X(double ENTER to stop): ")
    while True:#while user will not input "ENTER", he enters a list
        temp = input()
        if temp == "":
            break
        x.append(float(temp))
    y = linked_list()
    print("Input Y(double ENTER to stop): ")
    while True:#while user will not input "ENTER", he enters a list
        temp = input()

        if temp == "":
            break
        y.append(float(temp))
    result = create_z(x, y, x.len())#call a function to create list "z" according to task
    return result

def user_choice():
    while True:
        x = input("Input \"1\" for generating lists or input \"2\" to create your own lists(input smth else to quit): ")#user inputs his own choice how to create lists
        if x == "1":#user inputs only size
            print(input_with_N())
        if x == "2":#user inputs only lists
            print(input_without_N())
        if x != "1" and x != "2":#user can quit main menu
            return

def valide_input_data():
    check = False
    while not check: #create infinity loop in order to user finally input correct data
        try:
            user_choice() #main function
            check = True
        except ValueError:
            check = False
            print("N must be a natural number!")
        except (IndexError, TypeError):
            check = False
            print("Sizes of lists must be same!")
        except NameError:
            check = False
            print("\"From\" must be lower than \"To\"!")
            
def create_matrix(arr, n):#the function which do all tasks
    matrix = []
    for i in range(n):
        temp=[] #the main matrix
        for j in range(n):
            temp.append(pow(arr[j],i)) #create temporary array
        matrix.append(temp) #add temporary array to the matrix
    for z in range(n): #outputting
        print(matrix[z])

def validation_and_running():#the function for validating data
    check = False
    while not check:
        try: #try to catch an error
            arr = []
            N = float(input("Input N: "))
            assert N > 0
            assert N % int(N) == 0
            N = int(N)
            print("Input array: ")
            for i in range(N):
                arr.append(float(input()))
            create_matrix(arr,N) #call the main function
            check  = True
        except AssertionError:
            check = False
            print("N must be a natural number!")
        except IndexError:
            check = False
            print("Make sure, array's length and N are equal!")
        except (TypeError, ValueError):
            check = False
            print("You must input only numbers using \"ENTER\"(=_=)!")

def menu():#the function for infinity starting a program
    check = "1" #key
    while check == "1":
        validation_and_running() #call a function to validate data
        check = input("Input \"1\" to try again or something else to exit: ")
        
valide_input_data()#call a function to validate data
menu()
>>>>>> master