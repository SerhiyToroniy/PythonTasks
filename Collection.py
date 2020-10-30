import operator #import operator to use it in the sort method
import os.path
from SwiftTransfer4 import * #import class SwiftTransfer
from Validation import *
from decimal import Decimal

class Collection:

    def __init__(self): #initializating list
        self.data = []

    def add(self, var):#add and an object into the end of the collection
        self.data.append(var)

    def add_inputed(self):
        temp = SwiftTransfer()
        temp.setID(input("ID: "))
        temp.setIBAN_NUMBER(input("Iban number: "))
        temp.setACCOUNT_HOLDER(input("Account holder: "))
        temp.setAMOUNT(input("Amount: "))
        temp.setCURRENCY(input("Currency: "))
        temp.setFEE_AMOUNT(input("Fee amount: "))
        temp.setPAYMENT_DATE(input("Payment date: "))
        self.data.append(temp)

    def len(self): #return size of  the colection
        return len(self.data)

    def display(self): #print the collection
        for i in self.data: print(i, "\n")

    def clear(self):
        self.data.clear()

    def __getitem__(self, item): #to use []
        return self.data[item]

    def __str__(self): #to use "print(Collection()"
        result = ""
        for i in self.data:
            result+=str(i)+"\n"
        return result

    def insert(self, it, obj):
        self.data.insert(it,obj)

    def remove(self, obj):
        for i in self.data:
            if i == obj:    self.data.remove(i)

    def search(self, line):
        temp = []
        for i in self.data:
            check = False
            for j in dir(i):
                if not j.startswith("get") and not j.startswith("set") and not j.startswith("__") and (getattr(i,j).upper().find(line.upper())!=-1):  check = True #find any kind of our line
            if check:   temp.append(i) #
        if len(temp)==0: print("We couldn't find it :( ")
        else:
            for z in temp:  print(z, "\n") #print objects whose contain our line

    def sort(self, attr): #sort by an attribute of our object
        our_key = ""
        i = self.data[0]
        for j in dir(i):
            if not j.startswith("get") and not j.startswith("set") and not j.startswith("__") and (j.upper().find(attr.upper()) != -1):
                our_key = j
                break
        return sorted(self.data, key = operator.attrgetter(our_key)) #using "operator" to get an attribute name

    def delete_by_id(self, ident):#delete anobject by id
        check = True
        for i in self.data:
            if i.getID() == ident:
                self.data.remove(i)
                check = True
                break
            else: check = False
        if not check:   print("We couldn't find an object with this ID: ",ident,"!")
        return self.data

    def edit_by_id(self, ident): #edit object by inputed id
        check = True
        for i in range(len(self.data)):
            if self.data[i].getID() == ident:
                temp = SwiftTransfer()
                temp.setID(input("ID: "))
                temp.setIBAN_NUMBER(input("Iban number: "))
                temp.setACCOUNT_HOLDER(input("Account holder: "))
                temp.setAMOUNT(input("Amount: "))
                temp.setCURRENCY(input("Currency: "))
                temp.setFEE_AMOUNT(input("Fee amount: "))
                temp.setPAYMENT_DATE(input("Payment date: "))
                self.data.insert(i, temp)#insert an object before removing
                self.data.remove(self.data[i+1])
                check = True
                break
            else: check = False
        if not check:   print("We couldn't find an object with this ID: ",ident,"!")
        return self.data

def file_to_arr(mas, File, FileName): #the main function to get data from file
    lst = File.read().split("\n") #make a list of lines
    if lst[0] == "":
        print(FileName,"doesn't consist any data!")
        return None
    temp = SwiftTransfer()
    j = 0
    while j != len(lst):
        for i in dir(temp):
            if not i.startswith("get") and not i.startswith("set") and not i.startswith("__"):
                if i.upper().find("AMOUNT")!= -1:    lst[j] = str(round(Decimal(float(lst[j])),2))
                setattr(temp, i, lst[j])
                j += 1
        if validate_obj(temp):
            mas.add(temp)
        else: print("Object with name",str(temp.getACCOUNT_HOLDER()),"was skipped due to not valid data!")
        temp = SwiftTransfer()#create a new SwiftTransfer object every time

def arr_to_file(lst, File_name):
    File = open(File_name, "w") #check whether file exists was in #main
    for j in lst:  # updating data.txt file
        for h in dir(j):
            if not h.startswith("get") and not h.startswith("set") and not h.startswith("__"): File.writelines(getattr(j, h) + "\n")
    File.close()

def menu(lst, File_name):
    while True: #show menu after every user's choice
        choice = input("1 - find an object by inputed data\n2 - sort a collection by inputed data\n3 - delete object from the collection by id\n4 - add an object to the collection\n5 - edit an object in the collection by id\nNumber is your choice: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":   break
        if choice == "1":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            lst.search(input("SEARCH: "))
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
        if choice == "2":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            temp = lst.sort(input("SORT BY: "))
            arr_to_file(temp, File_name)
            for i in temp: print(i,"\n")
        if choice == "3":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            temp = lst.delete_by_id(input("Input ID to delete objects: "))
            arr_to_file(temp, File_name)
            for i in temp: print(i,"\n")
        if choice == "4":
            lst.add_inputed()
            if validate_lst(lst):
                lst.display()
                arr_to_file(lst, File_name)
            else: lst.remove(lst[lst.len()-1])
        if choice == "5":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            save = []
            for i in lst:   save.append(i)
            lst.edit_by_id(input("EDIT BY ID: "))
            if validate_lst(lst):
                lst.display()
                arr_to_file(lst, File_name)
            else:
                lst.clear()
                for i in save:  lst.add(i)
                lst.display()
                arr_to_file(lst, File_name)

def validate_obj(obj):
    try:
        if not Validation().digit_check(obj.getAMOUNT()) or not Validation().low_up_limit_check(obj.getAMOUNT(), -1):   raise TypeError
        if not Validation().digit_check(obj.getID()) or not Validation().low_up_limit_check(obj.getID(), -1):   raise TypeError
        if not Validation().digit_check(obj.getFEE_AMOUNT()) or not Validation().low_up_limit_check(obj.getFEE_AMOUNT(), -1, obj.getAMOUNT()):  raise TypeError
        if not Validation().char_check(obj.getCURRENCY()) or not Validation().space_count(obj.getCURRENCY(),0) or not Validation().currency_check(obj.getCURRENCY()): raise TypeError
        if not Validation().date_check(obj.getPAYMENT_DATE()):  raise TypeError
        if not Validation().iban_number_check(obj.getIBAN_NUMBER()):    raise TypeError
        if not Validation().char_check(obj.getACCOUNT_HOLDER()) or not Validation().space_count(obj.getACCOUNT_HOLDER(), 1):    raise TypeError
    except (TypeError, ValueError): return False
    except AttributeError:  return False
    return True

def validate_lst(lst): #the main validation function
    try:
        for i in range(lst.len()-1):  validate_obj(lst[i])
    except (TypeError,ValueError):
        print("\n=[Make sure, data type is correct and try again!]=\n")
        return False
    except AttributeError:
        print("\n=[Input correct attribute!]=\n")
        return False
    return True

if __name__ == "__main__":
    arr = Collection()
    file_name = input("Input name of data file: ")
    while not os.path.exists(file_name):
        file_name = input("FILE DOESN'T EXIST: ")
    else:
        file = open(file_name)
        file_to_arr(arr, file, file_name)
        file.close()
        menu(arr, file_name)
