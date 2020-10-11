class Validation:

    @staticmethod
    def digit_check(var):
        if not var.isdigit():     print(var, "'s not a number!")
        return var.isdigit()

    @staticmethod
    def low_up_limit_check(var, low = 0, up = 10**10):
        if float(var) < low:    print(var,"must be bigger than",low,"!")
        if float(var) > int(up):    print(var,"must be lower than",up,"!")
        return low < float(var) <= int(up)

    @staticmethod
    def char_check(var):
        if not ''.join(var.split()).isalpha(): print(var,"'s not a string!")
        return ''.join(var.split()).isalpha()#avoid SPACE

    @staticmethod
    def space_count(var, limit):
        count = 0
        for i in var:
            if i == " ": count += 1
        if count > limit:   print("Too many spaces in",var,"!")
        return count == limit

    @staticmethod
    def iban_number_check(var):
        if len(var)>19: print("Length of",var,"is so big!")
        if len(var)<19: print("Length of",var,"is so small!")
        if var[0] + var[1] != "UA": print("Iban number should start with \"UA\", not",var[0]+var[1],"!")
        valid  = True
        count = 0
        for i in var:
            if i == " ": count += 1
        if not count == 3: valid = False
        num_part = ""
        for i in range(len(var)-1):
            if i == 0 or i == 1 or var[i]==" ": continue
            num_part+=var[i]
        if not num_part.isdigit():  print(num_part, "cannot contain symbols!")
        return len(var)==19 and var[0] + var[1] == "UA" and valid and num_part.isdigit()

    @staticmethod
    def date_check(var):
        dot_count = 0
        dot1 = 4 #possible locations of dots
        dot2 = 7
        for i in range(len(var)-1):
            if var[i]==".":  dot_count+=1 #count dots
        if dot_count != 2:  print("Too many dots in",var,"!")
        if  var[0] == "." or var[len(var)-1] == "." or var[dot1] != "." or var[dot2] != ".":    print("Dots should be placed elsewhere in ",var,"!")
        for i in range(len(var)-1):
            if var[i] == "." and var[i-1] == ".":
                print("Dots should be placed elsewhere in",var,"!")
                return False
        number = month = year = ""
        for i in range(len(var)):
            if i == dot1 or i == dot2:    continue
            if i < dot1:   year+=var[i]
            if dot1 < i < dot2: month+=var[i]
            if i > dot2:   number+=var[i]
        if int(year) < 1 or int(year) > 2020:   print(int(year), "must be > 0 and <= 2020 in",var,"!")
        if int(month) < 1 or int(month) > 12:   print(int(month), "must be > 0 and <= 12 in",var,"!")
        if int(number) < 1 or int(number) > 31: print(int(number), "must be > 0 and <= 31 in",var,"!")
        return dot_count == 2 and not(var[0] == "." or var[len(var)-1] == "." or var[dot1] != "." or var[dot2] != ".") and not(int(year) < 1 or int(year) > 2020) and not(int(month) < 1 or int(month) > 12) and not(int(number) < 1 or int(number) > 31)
