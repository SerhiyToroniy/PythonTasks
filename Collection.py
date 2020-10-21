import operator #import operator to use it in the sort method
from SwiftTransfer import * #import class SwiftTransfer
from Validation_with_decorators import *
# from Validation import *
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
        temp = Collection()
        for i in self.data:
            temp.add(i)
        return temp


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
                if j[0]+j[1]!="ge" and j[0]+j[1]!="se" and j[0]+j[1]!="__"and (getattr(i,j).upper().find(line.upper())!=-1):  check = True #find any kind of our line
            if check:   temp.append(i) #
        if len(temp)==0: print("We couldn't find it :( ")
        else:
            for z in temp:  print(z, "\n") #print objects whose contain our line

    def sort(self, attr): #sort by an attribute of our object
        our_key = ""
        i = self.data[0]
        for j in dir(i):
            if j[0]+j[1]!="ge" and j[0]+j[1]!="se" and j[0]+j[1]!="__" and (j.upper().find(attr.upper()) != -1):
                our_key = j
                break
        if our_key != "":
            self.data = sorted(self.data, key = operator.attrgetter(our_key)) #using "operator" to get an attribute name
            temp = Collection()
            for i in self.data:
                temp.add(i)
            return temp
        else:
            temp = Collection()
            for i in self.data:
                temp.add(i)
            return temp

    @staticmethod
    def delete_by_id(ident, lst):#delete anobject by id
        check = True
        for i in lst:
            if i.getID() == ident:
                lst.remove(i)
                check = True
                break
            else: check = False
        if not check:
            print("We couldn't find an object with this ID: ",ident,"!")

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
        temp = Collection()
        for i in self.data:
            temp.add(i)
        return temp

def file_to_arr(mas, File, FileName): #the main function to get data from file
    lst = File.read().split("\n") #make a list of lines
    if lst[0] == "":
        print(FileName,"doesn't consist any data!")
        return None
    temp = SwiftTransfer()
    j = 0
    while j != len(lst):
        for i in dir(temp):
            if i[0]+i[1]!="ge" and i[0]+i[1]!="se" and i[0]+i[1]!="__":
                if i.upper().find("AMOUNT")!= -1:
                    dot = False
                    for p in lst[j]:
                        if p == ".":
                            dot = True
                            break
                    if dot:
                        lst[j] = str(round(Decimal(float(lst[j])),2))
                setattr(temp, i, lst[j])
                j += 1
        if validate_obj(temp):  mas.add(temp)
        else: print("Object with name",str(temp.getACCOUNT_HOLDER()),"was skipped due to not valid data!")
        temp = SwiftTransfer()#create a new SwiftTransfer object every time

def arr_to_file(lst, File_name):
    File = open(File_name, "w") #check whether file exists was in #main
    for j in lst:  # updating data.txt file
        for h in dir(j):
            if h[0]+h[1]!="ge" and h[0]+h[1]!="se" and h[0]+h[1]!="__": File.writelines(getattr(j, h) + "\n")
    File.close()

def validate_obj(obj):
    try:
        if not Validation().digit_check(str(obj.getAMOUNT())) or not Validation().low_up_limit_check(obj.getAMOUNT(),-1, 10**10):
            raise TypeError
        if not Validation().digit_check(obj.getID()) or not Validation().low_up_limit_check(obj.getID(), -1, 10**10):
            raise TypeError
        if not Validation().digit_check(str(obj.getFEE_AMOUNT())) or not Validation().low_up_limit_check(obj.getFEE_AMOUNT(), -1, obj.getAMOUNT()):
            raise TypeError
        if not Validation().char_check(obj.getCURRENCY()) or not Validation().space_count(obj.getCURRENCY(),0):
            raise TypeError
        if not Validation().date_check(obj.getPAYMENT_DATE()):
            raise TypeError
        if not Validation().iban_number_check(obj.getIBAN_NUMBER()):
            raise TypeError
        if not Validation().char_check(obj.getACCOUNT_HOLDER()) or not Validation().space_count(obj.getACCOUNT_HOLDER(), 1):
            raise TypeError
    except (TypeError, ValueError):
        print("\n=[Make sure, data type is correct and try again!]=\n")
        return False
    except AttributeError:
        print("\n=[Input correct attribute!]=\n")
        return False
    return True

def validate_lst(lst): #the main validation function
    for i in range(lst.len()):
        if not validate_obj(lst[i]):
            return False
    return True