from LinkedList import *
from Iterator import *
from Validation import *
import os.path
import operator

class Strategy:
    @staticmethod
    def insert(lst):
        pass

class ConcreteStrategyIterator(Strategy):
    @staticmethod
    def insert(lst):
        v = Validation()
        index = input("Index: ")
        while not v.digit_check(index):
            index = input("Index must be a positive number: ")
        index = int(index)
        while index != 0 and lst.length() == 0:
            index = input("Your list is empty, you can choose only \"0\" index: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
        while index > lst.length() or index < 0:
            index = input("Index must be in list range: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)

        limit = input("Input limit for iterator: ")
        while not v.digit_check(limit):
            limit = input("Limit must be a positive number: ")
        limit = int(limit)
        for i in MyIterator(limit):
            lst.insert(index, i)
            index+=1

class ConcreteStrategyFile(Strategy):
    @staticmethod
    def insert(lst):
        v = Validation()
        file_name = input("Input name of data file: ")
        while not os.path.exists(file_name):
            file_name = input("File doesn't exist: ")
        file = open(file_name)
        temp = file.read().split("\n")
        file.close()
        if temp[0] == "":
            print("FILE is empty!")
            return None
        correct = []
        for i in temp:
            if not v.positive_check(i): print(i,"was skipped because it's not a number!")
            else:
                dot = False
                for z in i:
                    if z==".":
                        dot = True
                        break
                if dot: correct.append(float(i))
                else: correct.append(int(i))
        index = input("Index: ")
        while not v.digit_check(index):
            index = input("Index must be a positive number: ")
        index = int(index)
        while index != 0 and lst.length() == 0:
            index = input("Your list is empty, you can choose only \"0\" index: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
        while index > lst.length() or index < 0:
            index = input("Index must be in list range: ")
            while not v.digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
        for i in correct:
            lst.insert(index, i)
            index += 1

class Contex:
    def __init__(self, strat: Strategy = None):
        self.strategy = strat
    def setStrategy(self, strat: Strategy):
        self.strategy = strat
    def execudeStrategy(self,lst):
        return self.strategy.insert(lst)