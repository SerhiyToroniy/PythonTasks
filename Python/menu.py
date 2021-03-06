from PatternStrategy import *
from LinkedList_task3 import *
from Validation import *

def menu():
    contex = Contex()
    List = LinkedList()
    v = Validation()
    while True:
        choice = input("1 - Use strategy 1 to insert into the list\n2 - Use strategy 2 to insert into the list\n3 - Generate data\n4 - Delete the item at the specified position\n5 - Delete multiple items within the start and end positions\n6 - Method for working with the list\n7 - Display a list\n8 - Exit\nYour choice is: ")
        while not v.digit_check(choice):
            choice = input("Choise must be a positive number: ")
        choice = int(choice)
        while not (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8):
            choice = input("Choise must be in range[1-8]: ")
            while not v.digit_check(choice):
                choice = input("Choise must be a number: ")
            choice = int(choice)
        if choice == 1:
            contex.setStrategy(ConcreteStrategyIterator())
        if choice == 2:
            contex.setStrategy(ConcreteStrategyFile())
        if choice == 3:
            if contex.getStrategy() is None:
                print("Choose a strategy first!")
                continue
            contex.execudeStrategy(List)
            List.display()
        if choice == 4:
            if List.length() == 0:
                print("Your list is empty!")
                continue
            index = input("Index: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
            while index > List.length() or index < 0:
                index = input("Index must be in list range: ")
                while not v.digit_check(index):
                    index = input("Index must be a positive number: ")
                index = int(index)
            List.erase(index)
        if choice == 5:
            if List.length() == 0:
                print("Your list is empty!")
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
                while start > List.length() or start < 0:
                    index = input("Start must be in list range: ")
                    while not v.digit_check(index):
                        index = input("Start must be a positive number: ")
                    start = int(start)
                end = input("END:")
                while not v.digit_check(end):
                    end = input("End must be a positive number: ")
                end = int(end)
                while end > List.length() or end < 0:
                    end = input("End must be in list range: ")
                    while not v.digit_check(end):
                        end = input("End must be a positive number: ")
                    end = int(end)
                first_iter = False
            List.cut(start,end)
        if choice == 6:
            if List.length() == 0:
                print("Your list is empty!")
                continue
            user_choice(List)
        if choice == 7:
            List.display()
        if choice == 8:
            break
menu()
