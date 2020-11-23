from Strategy import *
from LinkedList_task3 import *
from Validation import *
from LinkedList import *
from Contex import *
from ConcreteStrategyFile7 import *
from ConcreteStrategyIterator7 import *
from Logger import *
from Event import *
import concurrent.futures
import copy

def tothread(state, arrs, lists, names, _index, _e):
    savedList = copy.deepcopy(lists)
    results = []
    j = 0
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            if isinstance(_index, tuple):
                for i in range(len(lists)):
                    results.append(executor.submit(arrs[0], lists[i], _index[j], _index[j+1]))
                lists.reverse()
                for f in concurrent.futures.as_completed(results):
                    binary,lst = f.result()
                    _e.run(f"{state}({names[j]})", binary, lst, lists[j])
                    j += 1
            else:
                for i in arrs:
                    if isinstance(_index, list) and len(_index) > 1:results.append(executor.submit(i, _index[j], _index[j+1]))
                    else: results.append(executor.submit(i, _index))
                for p in concurrent.futures.as_completed(results):
                    if p.result() is None:
                        raise IndexError
                for f in concurrent.futures.as_completed(results):
                    _e.run(f"{state}({names[j]})", _index, f.result(), lists[j])
                    j += 1
    except IndexError:
        print("Index is out of range!")
        return savedList



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
            result = tothread("delete",[ListFile.erase, ListIterator.erase],[ListIterator, ListFile],["ListIterator","ListFile"],index, e)
            if not result is None:  ListIterator, ListFile = result
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
                while start >= ListFile.length() or start >= ListIterator.length() or start < 0:
                    start = input("Start must be in list range: ")
                    while not v.digit_check(start):
                        start = input("Start must be a positive number: ")
                    start = int(start)
                end = input("END:")
                while not v.digit_check(end):
                    end = input("End must be a positive number: ")
                end = int(end)
                while end >= ListFile.length() or end >= ListIterator.length() or end < 0:
                    end = input("End must be in list range: ")
                    while not v.digit_check(end):
                        end = input("End must be a positive number: ")
                    end = int(end)
                first_iter = False
            result = tothread("delete", [ListFile.cut, ListIterator.cut], [ListIterator, ListFile],["ListIterator", "ListFile"], [start,end], e)
            if not result is None:  ListIterator, ListFile = result
        if choice == 6:
            start = input("START:")
            while not v.digit_check(start):
                start = input("Start must be a positive number: ")
            start = int(start)
            end = input("END:")
            while not v.digit_check(end):
                end = input("End must be a positive number: ")
            end = int(end)
            tothread("changed", [user_choice], [ListFile, ListIterator], ["ListIterator", "ListFile"], (start,end), e)
        if choice == 7:
            print("ListFile:")
            ListFile.display()
            print("ListIterator:")
            ListIterator.display()
        if choice == 8:
            break
menu()
