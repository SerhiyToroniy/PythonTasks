from abc import ABC, abstractmethod
from random import sample
from string import ascii_letters, digits
from Collection import *
from Validation_with_decorators import *
import copy
import os.path

class Memento:
    @abstractmethod
    def get_state(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str, col) -> None:
        self._state = str(state)
        self._col = copy.deepcopy(col)

    def get_state(self) -> str:
        return self._state

    def get_col(self):
        return self._col

class Originator:
    _state = None
    _col = Collection()

    def __init__(self, state: str, col) -> None:
        self._state = state
        self._col = col

    def do_something(self, choice: str, File_name) -> None:
        if choice == "1":
            if os.stat(File_name).st_size == 0 or self._col.len() == 0:
                print("Your data file is empty as well as array!")
                return
            self._col.search(input("SEARCH: "))
        if choice == "2":
            if os.stat(File_name).st_size == 0 or self._col.len() == 0:
                print("Your data file is empty as well as array!")
                return
            self._col = self._col.sort(input("SORT BY: "))
            self._state = self._generate_random_string(10)
            arr_to_file(self._col, File_name)
            for i in self._col: print(i, "\n")
        if choice == "3":
            if os.stat(File_name).st_size == 0 or self._col.len() == 0:
                print("Your data file is empty as well as array!")
                return
            self._col.delete_by_id(input("Input ID to delete objects: "), self._col)
            self._state = self._generate_random_string(10)
            arr_to_file(self._col, File_name)
            for i in self._col: print(i, "\n")
        if choice == "4":
            temp = copy.deepcopy(self._col)
            self._col = self._col.add_inputed()
            self._state = self._generate_random_string(10)
            if validate_lst(self._col):
                self._col.display()
                arr_to_file(self._col, File_name)
            else:
                print("You tried to add invalid object!")
                self._col = temp
        if choice == "5":
            if os.stat(File_name).st_size == 0 or self._col.len() == 0:
                print("Your data file is empty as well as array!")
                return
            temp = copy.deepcopy(self._col)
            self._col = self._col.edit_by_id(input("EDIT BY ID: "))
            self._state = self._generate_random_string(10)
            if validate_lst(self._col):
                self._col.display()
                arr_to_file(self._col, File_name)
            else:
                print("Your new object isn't valid!")
                self._col = temp
        if choice == "8":
            self._col.display()


    @staticmethod
    def _generate_random_string(length: int = 10):
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state, self._col)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        self._col = memento.get_col()

class Caretaker:

    def __init__(self, origin: Originator) -> None:
        self._Umementos = []
        self._Rmementos = []
        self._originator = origin

    def backup(self) -> None:
        if len(self._Umementos) + len(self._Rmementos) > 5:
            print("You can remeber only 5 last actions!")
            self._Umementos.pop(-1)
            return
        self._Umementos.append(self._originator.save())


    def undo(self) -> None:
        if not len(self._Umementos):
            print("You can't use undo()!")
            return
        memento = self._Umementos.pop()
        self._Rmementos.append(self._originator.save())
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def redo(self) -> None:
        if len(self._Umementos) + len(self._Rmementos) > 5:
            print("You can remeber only 5 last actions!")
            return
        if len(self._Rmementos)<=len(self._Umementos) or not len(self._Rmementos):
            print("You can't use redo()!")
            return
        memento = self._Rmementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.redo()

def menu(lst, File_name):
    origin = Originator("first", lst)
    caretaker = Caretaker(origin)
    while True: #show menu after every user's choice
        choice = input("1 - find an object by inputed data\n2 - sort a collection by inputed data\n3 - delete object from the collection by id\n4 - add an object to the collection\n5 - edit an object in the collection by id\n6 - undo\n7 - redo\n8 - display\nNumber is your choice: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":   break
        if choice == "1":
            origin.do_something(choice, File_name)
        if choice == "2":
            caretaker.backup()
            origin.do_something(choice, File_name)
        if choice == "3":
            caretaker.backup()
            origin.do_something(choice, File_name)
        if choice == "4":
            caretaker.backup()
            origin.do_something(choice, File_name)
        if choice == "5":
            caretaker.backup()
            origin.do_something(choice, File_name)
        if choice == "6":
            caretaker.undo()
        if choice == "7":
            caretaker.redo()
        if choice == "8":
            origin.do_something(choice, File_name)

if __name__ == "__main__":
    arr = Collection()
    file_name = input("Input name of data file: ")
    if not os.path.exists(file_name):
        print("FILE \"", file_name, "\" DOESN'T EXIST!")
    else:
        file = open(file_name)
        file_to_arr(arr, file, file_name)
        file.close()
        menu(arr, file_name)