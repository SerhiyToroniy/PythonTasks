import unittest
import copy
from Collection6 import*

class TestCollection(unittest.TestCase):

    def setUp(self):
        #list from file
        self.arr = Collection()
        self.arr.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.arr.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        self.arr.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))

        #extra list for test_add/test_edit
        self.extra = Collection()
        self.extra.add(SwiftTransfer("00000", "UA00 0000 0000 0000", "Lomachenko Andriy", "12500.00", "usd", "565.00", "2010.01.11"))
        self.extra.add(SwiftTransfer("11111", "UA11 1111 1111 1111", "Tetyana Stoyko", "11567.00", "uah", "153.00", "2019.02.02"))
        self.extra.add(SwiftTransfer("22222", "UA22 2222 2222 2222", "Boyko Anatoliy", "22222.00", "eur", "557.00", "2018.02.27"))

        #list with ids from the file
        self.ListID = ["68292","67899","77777"]

        #Caretaker is used in test_undo/test_redo
        self.caretaker = Caretaker(self.arr)
        self.caretaker.backup()

    def test_readFromFile(self):
        file = open("data.txt")
        temp = Collection()
        file_to_arr(temp, file, "data.txt")
        file.close()

        self.assertEqual(self.arr, temp)
        self.assertIsInstance(temp,Collection)
        self.assertIsInstance(temp[0],SwiftTransfer)

    def test_writeToFile(self):
        arr_to_file(self.arr,"data2.txt")
        file = open("data2.txt")
        temp = Collection()
        file_to_arr(temp, file, "data2.txt")
        file.close()

        self.assertEqual(self.arr, temp)
        self.assertIsInstance(temp, Collection)
        self.assertIsInstance(temp[0], SwiftTransfer)

    def test_find(self):
        for i in range(len(self.ListID)-1):
            self.assertEqual(self.arr.search(self.ListID[i]), [self.arr[i]])

    def test_sort(self):
        unSorted = copy.deepcopy(self.arr)

        self.arr.sort("iban", self.arr)
        self.arr.sort("fee", self.arr)
        self.assertEqual(self.arr,unSorted)

        self.arr.sort("currency", self.arr)
        self.assertEqual(self.arr,unSorted)

    def test_delete(self):
        for i in range(len(self.ListID)):
            deletable = copy.deepcopy(self.arr[0])
            self.arr.delete_by_id(self.ListID[i])
            self.assertNotIn(deletable,self.arr)

    def test_add(self):
        for i in range(self.extra.len()):
            self.arr.add_inputed(self.arr, self.extra[i])
            self.assertIn(self.extra[i],self.arr)

    def test_edit(self):
        for i in range(self.extra.len()):
            changable = copy.deepcopy(self.arr[i])
            self.arr.edit_by_id(self.ListID[i], self.arr, self.extra[i])
            self.assertIn(self.extra[i],self.arr)
            self.assertNotIn(changable,self.arr)

    def test_undo(self):
        for i in range(len(self.ListID)):
            deletable = copy.deepcopy(self.arr[0])
            self.arr.delete_by_id(self.ListID[i])
            self.caretaker.backup()
            self.caretaker.undo()
            self.assertIn(deletable,self.arr)

    def test_redo(self):
        for i in range(len(self.ListID)):
            deletable = copy.deepcopy(self.arr[0])
            self.arr.delete_by_id(self.ListID[i])
            self.caretaker.backup()
            self.caretaker.undo()
            self.caretaker.redo()
            self.assertNotIn(deletable, self.arr)

if __name__ == "__main__":
    unittest.main()
