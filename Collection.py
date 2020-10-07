import operator #import operator to use it in the sort method
from SwiftTransfer import * #import class SwiftTransfer

class Collection:
    def __init__(self): #initializating list
        self.data = []

    def add(self, var):#add and an object into the end of the collection
        self.data.append(var)

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

    def insert(self, it, object):
        self.data.insert(it,object)

    def remove(self, object):
        for i in self.data:
            if i == object:
                self.data.remove(i)

    def search(self, line):
        temp = []
        for i in self.data:
            check = False
            for j in dir(i):
                if j[0]!="_" and (getattr(i,j).find(line.upper())!=-1 or getattr(i,j).find(line.lower())!=-1 or getattr(i,j).find(line)!=-1):  check = True #find any kind of our line
            if check:   temp.append(i) #
        if len(temp)==0: print("We couldn't find it :( ")
        else:
            for z in temp:  print(z, "\n") #print objects whose contain our line

    def sort(self, attr): #sort by an attribute of our object
        our_key = ""
        if len(self.data)!= 0:
            i = self.data[0]
            for j in dir(i):
                if j[0] != "_" and (j.find(attr.upper()) != -1 or j.find(attr.lower()) != -1 or j.find(attr) != -1):
                    our_key = j
                    break
        return sorted(self.data, key = operator.attrgetter(our_key)) #using "operator" to get an attribute name

    def delete_by_id(self, ident):#delete anobject by id
        for i in self.data:
            if i._getID() == ident:   self.data.remove(i)
        return self.data

    def edit_by_id(self, ident): #edit object by inputed id
        for i in range(len(self.data)):
            if self.data[i]._getID() == ident:
                self.data.insert(i, self.data[i]._input())#insert an object before removing
                self.data.remove(self.data[i+1])
        return self.data
