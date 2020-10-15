class Validation:

    def decor_date_check(f):
        def inner(*args):
            dot_count = 0
            dot1 = 4  # possible locations of dots
            dot2 = 7
            for i in range(len(args[0]) - 1):
                if args[0][i] == ".":  dot_count += 1  # count dots
            if dot_count != 2:  print("Too many dots in", args[0], "!")
            if args[0][0] == "." or args[0][len(args[0]) - 1] == "." or args[0][dot1] != "." or args[0][dot2] != ".":    print("Dots should be placed elsewhere in ", args[0], "!")
            for i in range(len(args[0]) - 1):
                if args[0][i] == "." and args[0][i - 1] == ".":
                    print("Dots should be placed elsewhere in", args[0], "!")
                    return False
            number = month = year = ""
            for i in range(len(args[0])):
                if i == dot1 or i == dot2:    continue
                if i < dot1:   year += args[0][i]
                if dot1 < i < dot2: month += args[0][i]
                if i > dot2:   number += args[0][i]
            if int(year) < 1 or int(year) > 2020:   print(int(year), "must be > 0 and <= 2020 in", args[0], "!")
            if int(month) < 1 or int(month) > 12:   print(int(month), "must be > 0 and <= 12 in", args[0], "!")
            if int(number) < 1 or int(number) > 31: print(int(number), "must be > 0 and <= 31 in", args[0], "!")
            res = f(args[0]) and dot_count == 2 or var[dot1] != "." or var[dot2] != "." and not (int(year) < 1 or int(year) > 2020) and not (int(month) < 1 or int(month) > 12) and not (int(number) < 1 or int(number) > 31)
            return res
        return inner

    def decor_iban_number_check(f):
        def inner(x):
            var = x
            if len(var) > 19: print("Length of", var, "is so big!")
            if len(var) < 19: print("Length of", var, "is so small!")
            if var[0] + var[1] != "UA": print("Iban number should start with \"UA\", not", var[0] + var[1], "!")
            count = 0
            valid = True
            for i in var:
                if i == " ": count += 1
            if not count == 3:
                print("Too many spaces in",var,"!")
                valid = False
            num_part = ""
            for i in range(len(var) - 1):
                if i == 0 or i == 1 or var[i] == " ": continue
                num_part += var[i]
            if not num_part.isdigit():
                print(num_part, "cannot contain symbols!")
            res = f(var) and valid and num_part.isdigit()
            return res
        return inner

    def decor_space_count(f):
        def inner(*args): #var, limit
            count = 0
            for i in args[0]:
                if i == " ": count += 1
            if count > args[1]:   print("Too many space in", args[0], "!")
            res = f(count,args[1])
            return res
        return inner

    def decor_char_check(f):
        def inner(x):
            var = x
            if not ''.join(var.split()).isalpha(): print(var, "'s not a string!")
            res = f(x)
            return res
        return inner

    def decor_low_up_limit_check(f):
        def inner(*args):
            if float(args[0]) < float(args[1]):    print(args[0], "must be bigger than", float(args[1]), "!")
            if float(args[0]) > float(args[2]):    print(args[0], "must be lower than", float(args[2]), "!")
            res = f(args[0],float(args[1]),float(args[2]))
            return res
        return inner

    def decor_digit_check(f):
        def inner(x):
            var = x
            count = 0
            for i in var:
                if i == ".": count += 1
            if not count <= 1:
                print("Too many dots in", var, "!")
                return False
            save = ""
            if count == 1:
                for i in var:
                    if i != '.':    save += i
                x = save
            if not x.isdigit():     print(var, "'s not a number!")
            res = f(x)
            return res
        return inner

    @staticmethod
    @decor_digit_check
    def digit_check(var):
        return var.isdigit()

    @staticmethod
    @decor_low_up_limit_check
    def low_up_limit_check(var, low, up):
        return low < float(var) <= float(up)

    @staticmethod
    @decor_char_check
    def char_check(var):
        return ''.join(var.split()).isalpha()#avoid SPACE

    @staticmethod
    @decor_space_count
    def space_count(var, limit):
        return var == limit

    @staticmethod
    @decor_iban_number_check
    def iban_number_check(var):
        return len(var) == 19 and var[0] + var[1] == "UA"

    @staticmethod
    @decor_date_check
    def date_check(var):
        return not(var[0] == "." or var[len(var)-1] == ".")
