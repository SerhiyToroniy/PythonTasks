from enums import Currency

class Validation:

    @staticmethod
    def currency_check(func):
        def inner(self, var):
            check = False
            for cur in Currency:
                if var.lower() == cur.name:
                    check = True
            if not check:
                print("Currency must be only uah, eur and usd but not",var,"!")
                return False
            func(self,var)
            return True
        return inner

    @staticmethod
    def iban_number_check(func):
        def inner(self, var):
            if len(var) > 19:
                print("Length of", var, "is so big!")
                return False
            if len(var) < 19:
                print("Length of", var, "is so small!")
                return False
            if var[0] + var[1] != "UA":
                print("Iban number should start with \"UA\", not", var[0] + var[1], "!")
                return False
            count = 0
            for i in var:
                if i == " ": count += 1
            if not count == 3:
                print("Too much spaces in",var,"!")
                return False
            num_part = ""
            for i in range(len(var) - 1):
                if i == 0 or i == 1 or var[i] == " ": continue
                num_part += var[i]
            if not num_part.isdigit():
                print(num_part, "cannot contain symbols!")
                return False
            if func(self, var) is None:
                return True
            else:
                return func(self, var)
        return inner

    @staticmethod
    def digit_check(func):
        def inner(self, var):
            count = 0
            for i in var:
                if i == ".": count += 1
            if not count <= 1:
                print("Too many dots in", var, "!")
                return False
            save = ""
            if count <= 1:
                for i in var:
                    if i != '.':    save += i
                x = save
                if not x.isdigit():
                    print(var, "'s not a number!")
                    return False
                else:
                    if func(self, var) is None:
                        return True
                    else:
                        return func(self, var)
        return inner

    @staticmethod
    def date_check(func):
        def inner(self, var):
            dot_count = 0
            dot1 = 4  # possible locations of dots
            dot2 = 7
            for i in range(len(var) - 1):
                if var[i] == ".":  dot_count += 1  # count dots
            if dot_count != 2:
                print("Too many dots in", var, "!")
                return False
            if var[0] == "." or var[len(var) - 1] == "." or var[dot1] != "." or var[dot2] != ".":
                print("Dots should be placed elsewhere in ", var, "!")
                return False
            for i in range(len(var) - 1):
                if var[i] == "." and var[i - 1] == ".":
                    print("Dots should be placed elsewhere in", var, "!")
                    return False
            number = month = year = ""
            for i in range(len(var)):
                if i == dot1 or i == dot2:    continue
                if i < dot1:   year += var[i]
                if dot1 < i < dot2: month += var[i]
                if i > dot2:   number += var[i]
            if int(year) < 1 or int(year) > 2020:
                print(int(year), "must be > 0 and <= 2020 in", var, "!")
                return False
            if int(month) < 1 or int(month) > 12:
                print(int(month), "must be > 0 and <= 12 in", var, "!")
                return False
            if int(number) < 1 or int(number) > 31:
                print(int(number), "must be > 0 and <= 31 in", var, "!")
                return False
            if func(self, var) is None:
                return True
            else:
                return func(self, var)
        return inner

    @staticmethod
    def low_up_limit_check(func):
        def inner(self, var):
            if float(var) < 0:
                print(var, "must be bigger than", low, "!")
                return False
            if func(self, var) is None:
                return True
            else:
                return func(self, var)
        return inner

    @staticmethod
    def char_check(func):
        def inner(self, var):
            if ''.join(var.split()).isalpha():
                return func(self,var)
            else:
                print(var, "isn't a string!")
                return False
        return inner

    @staticmethod
    def name_check(func):
        def inner(self, var):
            count = 0
            for i in var:
                if i == " ": count += 1
            if count!=1:
                print("Use SPACE between name and surname!")
                return False
            if func(self, var) is None:
                return True
            else:
                return func(self, var)
        return inner

    @staticmethod
    def space_count(func):
        def inner(self, var):
            count = 0
            for i in var:
                if i == " ": count += 1
            if count > 1:
                print("Too many space in", var, "!")
                return False
            else:
                return func(self,var)
        return inner