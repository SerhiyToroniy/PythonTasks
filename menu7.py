from Strategy import *
from LinkedList_task3 import *
from Validation import *
from LinkedList import *
from Contex import *
from ConcreteStrategyFile7 import *
from ConcreteStrategyIterator7 import *
from Logger import *
from Event import *
import threading
import copy

def menu():
    e = Event()
    o = Observer()
    log = Logger()
    o.attach("add(ListFile)", log.printToFile)
    o.attach("add(ListIterator)", log.printToFile)
    o.attach("delete(ListFile)", log.printToFile)
    o.attach("delete(ListIterator)", log.printToFile)
    o.attach("changed(ListFile)", log.printToFile)
    o.attach("changed(ListIterator)", log.printToFile)
    contex = Contex()
    ListFile = LinkedList()
    ListIterator = LinkedList()
    v = Validation()
    print("[Generating list using iterator]")
    contex.setStrategy(ConcreteStrategyIterator())
    contex.execudeStrategy(ListIterator)
    ListIterator.display()
    print("[Generating list using file]")
    contex.setStrategy(ConcreteStrategyFile())
    contex.execudeStrategy(ListFile)
    ListFile.display()
    while True:
        choice = input("4 - Delete the item at the specified position\n5 - Delete multiple items within the start and end positions\n6 - Method for working with the list\n7 - Display a list\n8 - Exit\nYour choice is: ")
        while not v.digit_check(choice):
            choice = input("Choise must be a positive number: ")
        choice = int(choice)
        while not (choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8):
            choice = input("Choise must be in range[1-8]: ")
            while not v.digit_check(choice):
                choice = input("Choise must be a number: ")
            choice = int(choice)
        if choice == 4:
            if ListFile.length() == 0 or ListIterator.length() == 0:
                print("One of lists is empty!")
                continue
            index = input("Index: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
            while index > ListFile.length() or index > ListIterator.length() or index < 0:
                index = input("Index is out of list range: ")
                while not v.digit_check(index):
                    index = input("Index must be a positive number: ")
                index = int(index)
            saveListIterator = copy.deepcopy(ListIterator)
            saveListFile = copy.deepcopy(ListFile)
            p1 = threading.Thread(target=ListIterator.erase, args=[index])
            p2 = threading.Thread(target=ListFile.erase, args=[index])
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            if saveListIterator.length() == ListIterator.length() or saveListFile.length() == ListFile.length():
                ListIterator=saveListIterator
                ListFile=saveListFile
                print("Index is out of range!")
            else:
                e.run("delete(ListIterator)", index, ListIterator, saveListIterator)
                e.run("delete(ListFile)", index, ListFile, saveListFile)
        if choice == 5:
            if ListFile.length() == 0 or ListIterator.length() == 0:
                print("One of lists is empty!")
                continue
            start = 1
            end = 0
            first_iter = True
            while start > end or first_iter:
                if not first_iter:
                    print("MAKE SURE, START <= END")
                start = input("START:")
                while not v.digit_check(start):
                    start = input("Start must be a positive number: ")
                start = int(start)
                while start > ListFile.length() or start > ListIterator.length() or start < 0:
                    index = input("Start must be in list range: ")
                    while not v.digit_check(index):
                        index = input("Start must be a positive number: ")
                    start = int(start)
                end = input("END:")
                while not v.digit_check(end):
                    end = input("End must be a positive number: ")
                end = int(end)
                while end > ListFile.length() or end > ListIterator.length() or end < 0:
                    end = input("End must be in list range: ")
                    while not v.digit_check(end):
                        end = input("End must be a positive number: ")
                    end = int(end)
                first_iter = False
                saveListIterator = copy.deepcopy(ListIterator)
                saveListFile = copy.deepcopy(ListFile)
                p1 = threading.Thread(target=ListIterator.cut, args=[start,end])
                p2 = threading.Thread(target=ListFile.cut, args=[start,end])
                p1.start()
                p2.start()
                p1.join()
                p2.join()
                if saveListIterator.length() == ListIterator.length() or saveListFile.length() == ListFile.length():
                    ListIterator = saveListIterator
                    ListFile = saveListFile
                    print("Index is out of range!")
                else:
                    e.run("delete(ListIterator)", list(range(start, end + 1)), ListIterator, saveListIterator)
                    e.run("delete(ListFile)", list(range(start, end + 1)), ListFile, saveListFile)
        if choice == 6:
            if ListFile.length() == 0 or ListIterator.length() == 0:
                print("One of lists is empty!")
                continue
            saveListIterator = copy.deepcopy(ListIterator)
            saveListFile = copy.deepcopy(ListFile)
            p1 = threading.Thread(target=user_choice, args=[ListIterator])
            p1.start()
            p1.join()
            p2 = threading.Thread(target=user_choice, args=[ListFile])
            p2.start()
            p2.join()
            e.run("changed(ListIterator)",0,ListIterator, saveListIterator)
            e.run("changed(ListFile)",0,ListFile, saveListFile)
        if choice == 7:
            print("ListFile:")
            ListFile.display()
            print("ListIterator:")
            ListIterator.display()
        if choice == 8:
            break
menu()