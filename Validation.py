from Collection import *

class Validation:
    def __init__(self, data = None):
        self.data = data

    def digit_check(self, var):
        return var.isdigit()

    def low_up_limit_check(self, var, low = 0, up = 10**10):
        return float(var) > low and float(var) < int(up)

    def char_check(self, var):
        space_count = 0
        for i in var:
            if i==" ": space_count+=1
            if space_count>1: #if SPACES more then enough
                return False
        return ''.join(var.split()).isalpha()#avoid SPACE

    def date_check(self, var):
        dot_count = 0
        dot1 = 4 #possible locations of dots
        dot2 = 7
        if  var[0] == "." or var[len(var)-1] == "." or var[dot1] != "." or var[dot2] != ".": #return False if dots are located elsewhere
            return False
        number = month = year = ""
        for i in range(len(var)):
            if i == dot1 or i == dot2:    continue
            if i < dot1:   year+=var[i]
            if i > dot1 and i < dot2: month+=var[i]
            if i > dot2:   number+=var[i]
        if int(year) < 0 or (int(month) < 1 or int(month) > 12) or (int(number) < 1 or int(number) > 31): return False #avoid 5678 number of month/date number, etc.
        for i in range(len(var)):
            if var[i]=="." and var[i-1]!="." and var[i+1]!=".":  dot_count+=1 #count dots
        return dot_count == 2

def file_to_arr(arr, file): #the main function to get data from file
    lst = file.read().split("\n") #make a list of lines
    temp = SwiftTransfer()
    j = 0
    while j != len(lst):
        for i in dir(temp):
            if i[0] != "_":
                setattr(temp, i, lst[j])
                j += 1
        arr.add(temp)
        temp = SwiftTransfer()#create a new SwiftTransfer object every time

def arr_to_file(arr):
    file = open("data.txt", "w")
    for j in arr:  # updating data.txt file
        for h in dir(j):
            if h[0] != "_":
                file.writelines(getattr(j, h) + "\n")
    file.close()

def menu(lst):
    while True: #show menu after every user's choice
        choice = input("1 - find an object by inputed data\n2 - sort a collection by inputed data\n3 - delete object from the collection by id\n4 - add an object to the collection\n5 - edit an object in the collection by id\nNumber is your choice: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            break
        if choice == "1":
            lst.search(input("SEARCH: "))
        if choice == "2":
            temp = lst.sort(input("SORT BY: "))
            arr_to_file(temp)
            for i in temp: print(i,"\n")
        if choice == "3":
            temp = lst.delete_by_id(input("Input ID to delete objects: "))
            arr_to_file(temp)
            for i in temp: print(i,"\n")
        if choice == "4":
            lst.add(SwiftTransfer()._input())
            if validate_and_run(False, lst):
                lst.display()
                arr_to_file(lst)
            else: lst.remove(lst[lst.len()-1])
        if choice == "5":
            ident = input("EDIT BY ID: ")
            save = SwiftTransfer()
            for i in lst:
                if i._getID() == ident: save = i
            lst.edit_by_id(ident)
            if validate_and_run(False, lst):
                lst.display()
                arr_to_file(lst)
            else:
                lst.remove(save)

def validate_and_run(check,arr): #the main validation function
    try:
        v = Validation()
        if check:
            # create objects
            file = open("data.txt")
            file_to_arr(arr, file)
            file.close()
        else:
            for i in arr:  # chech every object from data.txt
                if not v.digit_check(i._getAMOUNT()) or not v.low_up_limit_check(i._getAMOUNT(), -1):
                    raise TypeError
                if not v.digit_check(i._getID()) or not v.low_up_limit_check(i._getID(), -1):
                    raise TypeError
                if not v.digit_check(i._getFEE_AMOUNT()) or not v.low_up_limit_check(i._getFEE_AMOUNT(), -1,i._getAMOUNT()):
                    raise TypeError
                if not v.char_check(i._getCURRENCY()):
                    raise TypeError
                if v.char_check(i._getPAYMENT_DATE()) or v.digit_check(i._getPAYMENT_DATE()) or not v.date_check(i._getPAYMENT_DATE()):
                    raise TypeError
                if v.char_check(i._getIBAN_NUMBER()) or v.digit_check(i._getIBAN_NUMBER()):
                    raise TypeError
                if not v.char_check(i._getACCOUNT_HOLDER()):
                    raise TypeError
            return True
        menu(arr)
    except (TypeError,ValueError):
        print("\n=[Make sure, data type is correct and try again!]=\n")
    except AttributeError:
        print("\n=[Input correct attribute!]=\n")

arr = Collection()
validate_and_run(True, arr)
