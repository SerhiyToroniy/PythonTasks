class Validation:

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
            result = Validation().digit_check(wo_minusdots) and dot_count<=1
        else: return False
        return result