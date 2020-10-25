from Validation import *
from Strategy import *
import os.path

class ConcreteStrategyFile(Strategy):

    @staticmethod
    @Validation.file_check
    @Validation.index_check
    def insert(lst, filename, index):
        file = open(filename)
        temp = file.read().split("\n")
        file.close()
        if temp[0] == "":
            print("FILE is empty!")
            return
        correct = []
        for i in temp:
            if not Validation().positive_check(i):  print(i, "was skipped because it's not a number!")
            else:
                dot = False
                for z in i:
                    if z == ".":
                        dot = True
                        break
                if dot: correct.append(float(i))
                else:   correct.append(int(i))
        for i in correct:
            lst.insert(index, i)
            index += 1