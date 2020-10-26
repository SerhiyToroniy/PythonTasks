import operator #import operator to use it in the sort method
import os.path
import copy
from SwiftTransfer import * #import class SwiftTransfer
from decimal import Decimal
from Validation_with_decorators import *

class Collection:

    def __init__(self): #initializating list
        self.data = []

    def add(self, var):#add and an object into the end of the collection
        self.data.append(var)

    @staticmethod
    def add_inputed(lst):
        temp = SwiftTransfer()
        bools = [temp.setID(input("ID: ")), temp.setIBAN_NUMBER(input("Iban number: ")),
                 temp.setACCOUNT_HOLDER(input("Account holder: ")), temp.setAMOUNT(input("Amount: ")),
                 temp.setCURRENCY(input("Currency: ")), temp.setFEE_AMOUNT(input("Fee amount: ")),
                 temp.setPAYMENT_DATE(input("Payment date: "))]
        if all(bools):
            lst.add(temp)
            return temp
        return False

    def len(self): #return size of  the colection
        return len(self.data)

    def display(self): #print the collection
        for i in self.data: print(i, "\n")

    def clear(self):
        self.data.clear()

    def __getitem__(self, item): #to use []
        return self.data[item]

    def __str__(self): #to use "print(Collection())"
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
                if not j.startswith("get") and not j.startswith("set") and not j.startswith("__") and (getattr(i,j).upper().find(line.upper())!=-1):#skip setters/getter/magic methods in SwiftTranfer
                    check = True #find any kind of our line
            if check:   temp.append(i) #
        if len(temp)==0:
            print("We couldn't find it :( ")
        for z in temp:  print(z, "\n") #print objects whose contain our line

    def sort(self, attr): #sort by an attribute of our object
        our_key = ""
        i = self.data[0]
        for j in dir(i):
            if not j.startswith("get") and not j.startswith("set") and not j.startswith("__") and (j.upper().find(attr.upper()) != -1):#skip setters/getter/magic methods in SwiftTranfer
                our_key = j
                break
        return sorted(self.data, key = operator.attrgetter(our_key)) #using "operator" to get an attribute name

    def delete_by_id(self, ident):#delete an object by id
        check = True
        for i in self.data:
            if i.getID() == ident:
                self.data.remove(i)
                check = True
                break
            else: check = False
        if not check:   print("We couldn't find an object with this ID: ",ident,"!")
        return self.data

    def edit_by_id(self, ident, lst): #edit object by inputed id
        check = True
        copylst = copy.deepcopy(lst)
        obj = Collection().add_inputed(copylst)
        if type(obj) == bool:
            print("Object is invalid!")
            return False
        for i in range(len(self.data)):
            if self.data[i].getID() == ident:
                    self.data.insert(i, obj)  # insert an object before removing
                    self.data.remove(self.data[i + 1])
                    check = True
                    break
            else: check = False
        if not check:
            print("We couldn't find an object with this ID: ",ident,"!")
            return False
        return True


def file_to_arr(mas, File, FileName): #the main function to get data from file
    lst = File.read().split("\n") #make a list of lines
    if lst[0] == "":
        print(FileName,"doesn't consist any data!")
        return
    temp = SwiftTransfer()
    j = 0
    while j < len(lst):
        check = True

        #idk how to use a cycle below :(

        if not temp.setACCOUNT_HOLDER(lst[j]):
            check = False
        j += 1
        if not temp.setAMOUNT(lst[j]):
            check = False
        else:
            lst[j] = str(round(Decimal(float(lst[j])), 2))  # round amount and fee_amount if it's necessary
            temp.setAMOUNT(lst[j])
        j += 1
        if not temp.setCURRENCY(lst[j]):
            check = False
        j += 1
        if not temp.setFEE_AMOUNT(lst[j]):
            check = False
        else:
            lst[j] = str(round(Decimal(float(lst[j])), 2))  # round amount and fee_amount if it's necessary
            temp.setFEE_AMOUNT(lst[j])
        j += 1
        if not temp.setIBAN_NUMBER(lst[j]):
            check = False
        j += 1
        if not temp.setID(lst[j]):
            check = False
        j += 1
        if not temp.setPAYMENT_DATE(lst[j]):
            check = False
        j += 1
        if check:
            mas.add(temp)
        else:
            print("Object with name",str(temp.getACCOUNT_HOLDER()),"was skipped due to not valid data!")
        temp = SwiftTransfer()#create a new SwiftTransfer object every time

def arr_to_file(lst, File_name):
    File = open(File_name, "w") #check whether file exists was in #main
    for j in lst:  # updating data.txt file
        for h in dir(j):
            if not h.startswith("get") and not h.startswith("set") and not h.startswith("__"):
                File.writelines(getattr(j, h) + "\n")#skip setters/getter/magic methods in SwiftTranfer
    File.close()
