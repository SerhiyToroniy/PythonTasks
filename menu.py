from MyIterator import kaprekars_nums
from MyGenerator import validation #importing modules

def menu():
    while True:
        check = input("Choose an option(1 - do task using my generator/2 - do task using my iterator): ")
        if check != '1' and check != '2':
            break
        if check == '1':
            validation() #a function from MyGenerator module
        if check == '2':
            kaprekars_nums() #a function from MyIterator module
menu()
