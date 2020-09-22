import random #for generating random nums

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
        x = i#uodating x

def create_z(x, y, N):
    z = []
    i = 0 #iterator to compare lists
    while i < N:#create z according to the task
        if x[i] > y[i]:
            z.append("1")
        else:
            z.append("0")
        i += 1
    if len(z) == 0:#if lengths of lists aren't same, ValueError will be raise
        raise ValueError
    print("X: ",x)#outputting lists
    print("Y: ",y)
    print("Z: ",z)
    binary = "".join(z)#list z -> string z
    return find_demical(binary)#call function to find out a decimal num

def input_with_N():
    x = []
    y = []
    N = int(input("Input N: "))
    for i in range(N):#generate nums for "x"
        x.append(random.randint(-1000,1000))
    for j in range(N):#generate nums for "y"
        y.append(random.randint(-1000,1000))
    result = create_z(x, y, N)
    return result

def input_without_N():
    x = []
    print("Input X(double ENTER to stop): ")
    while True:#while user will not input "ENTER", he enters a list
        temp = input()
        if temp == "":
            break
        x.append(float(temp))
    y = []
    print("Input Y(double ENTER to stop): ")
    while True:#while user will not input "ENTER", he enters a list
        temp = input()
        if temp == "":
            break
        y.append(float(temp))
    result = create_z(x, y, len(x))#call a function to create list "z" according to task
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
        except IndexError:
            check = False
            print("Sizes of lists must be same!")

valide_input_data()#call a function to validate data
