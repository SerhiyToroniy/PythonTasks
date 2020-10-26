from Collection5 import *
import copy

def menu(lst, File_name):
    while True: #show menu after every user's choice
        choice = input("1 - find an object by inputed data\n2 - sort a collection by inputed data\n3 - delete object from the collection by id\n4 - add an object to the collection\n5 - edit an object in the collection by id\nNumber is your choice: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":   break
        if choice == "1":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            lst.search(input("SEARCH: "))
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
        if choice == "2":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            temp = lst.sort(input("SORT BY: "))
            arr_to_file(temp, File_name)
            for i in temp: print(i,"\n")
        if choice == "3":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            temp = lst.delete_by_id(input("Input ID to delete objects: "))
            arr_to_file(temp, File_name)
            for i in temp: print(i,"\n")
        if choice == "4":
            obj = lst.add_inputed(lst)
            if type(obj) != bool:
                lst.display()
                arr_to_file(lst, File_name)
        if choice == "5":
            if os.stat(File_name).st_size == 0 or lst.len() == 0:
                print("Your data file is empty as well as array!")
                continue
            if lst.edit_by_id(input("EDIT BY ID: "), lst):
                lst.display()
                arr_to_file(lst, File_name)

if __name__ == "__main__":
    arr = Collection()
    file_name = input("Input name of data file: ")
    while not os.path.exists(file_name):
        file_name = input("FILE DOESN'T EXIST: ")
    else:
        file = open(file_name)
        file_to_arr(arr, file, file_name)
        file.close()
        menu(arr, file_name)
