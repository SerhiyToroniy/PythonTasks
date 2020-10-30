import os.path

class Validation:

    @staticmethod
    def index_check(func):
        def inner(lst, filename, index):
            index = input("Index: ")
            while not Validation().digit_check(index):
                index = input("Index must be a positive number: ")
            index = int(index)
            while index != 0 and lst.length() == 0:
                index = input("Your list is empty, you can choose only \"0\" index: ")
                while not Validation().digit_check(index):
                    index = input("Index must be a positive number: ")
                index = int(index)
            while index > lst.length() or index < 0:
                index = input("Index must be in list range: ")
                while not Validation().digit_check(index):
                    index = input("Index must be a positive number: ")
                index = int(index)
            func(lst,filename, index)
        return inner

    @staticmethod
    def file_check(func):
        def inner(lst, filename, index):
            filename = input("Input name of data file: ")
            while not os.path.exists(filename):
                filename = input("File doesn't exist: ")
            func(lst, filename, index)
        return inner

    @staticmethod
    def limit_check(func):
        def inner(lst, limit, index):
            limit = input("Input limit for iterator: ")
            while not Validation().digit_check(limit):
                limit = input("Limit must be a positive number: ")
            func(lst, limit, index)
        return inner


    @staticmethod
    def digit_check(var):
        return var.isdigit()

    @staticmethod
    def positive_check(var):
        minus_count = 0
        dot_count = 0
        for i in var:
            if i == "-":    minus_count+=1
            if i == ".":    dot_count+=1
        wo_minusdots = ""
        if minus_count <=1:
            for i in var:
                if i == "-" or i == ".": continue
                wo_minusdots+=i
            for i in wo_minusdots:
                if not i.isdigit():
                    return False
            if minus_count > 0:
                return var[0] == "-"
            dot_position = True
            if dot_count > 0:
                dot_position = (var[0]!="." and var[len(var)-1]!=".")
            result = Validation().digit_check(wo_minusdots) and dot_count<=1 and dot_position
        else: return False
        return result
