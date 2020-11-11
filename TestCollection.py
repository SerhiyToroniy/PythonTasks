import unittest
from Collection6 import*

class TestCollection(unittest.TestCase):

    def setUp(self):
        self.arr = Collection()
        self.arr.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.arr.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        self.arr.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))


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
        self.assertEqual(self.arr.search("Tor"),[self.arr[0]])
        self.assertEqual(self.arr.search("eur"),[self.arr[0],self.arr[1],self.arr[2]])

        self.assertNotEqual(self.arr.search("tor"),[self.arr[1]])
        self.assertNotEqual(self.arr.search("7777"),[self.arr[1]])

    def test_sort(self):
        unCorrect = Collection()
        for i in range(self.arr.len()):
            unCorrect.add(self.arr[i])

        self.arr.sort("iban", self.arr)
        self.arr.sort("fee", self.arr)
        self.assertEqual(self.arr,unCorrect)

        self.arr.sort("currency", self.arr)
        self.assertEqual(self.arr,unCorrect)


    def test_delete(self):
        self.arr.delete_by_id("77777")
        self.assertNotIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"), self.arr)

        self.arr.delete_by_id("67899")
        self.assertNotIn(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"), self.arr)

    def test_add(self):
        self.arr.add_inputed(self.arr, SwiftTransfer("55555", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))
        self.assertIn(SwiftTransfer("55555", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"), self.arr)

        self.arr.add_inputed(self.arr, SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.assertIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"), self.arr)

        self.arr.add_inputed(self.arr, SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.assertIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"), self.arr)

    def test_edit(self):
        self.arr.edit_by_id("77777", self.arr, SwiftTransfer("77777", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))
        self.assertNotIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"),self.arr)
        self.assertIn(SwiftTransfer("77777", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"),self.arr)

        self.arr.edit_by_id("68292", self.arr, SwiftTransfer("68292", "UA22 2222 2222 2222", "Toroniy Ivan", "30000.00", "usd", "600.00", "2018.09.17"))
        self.assertNotIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"),self.arr)
        self.assertIn(SwiftTransfer("68292", "UA22 2222 2222 2222", "Toroniy Ivan", "30000.00", "usd", "600.00", "2018.09.17"),self.arr)

    def test_undo(self):
        caretaker = Caretaker(self.arr)
        caretaker.backup()
        self.arr.delete_by_id("77777")
        caretaker.backup()
        caretaker.undo()
        self.assertIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"),self.arr)
        self.arr.delete_by_id("68292")
        caretaker.backup()
        caretaker.undo()
        self.assertIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"),self.arr)

    def test_redo(self):
        caretaker = Caretaker(self.arr)
        caretaker.backup()
        self.arr.delete_by_id("77777")
        caretaker.backup()
        caretaker.undo()
        caretaker.redo()
        caretaker.undo()
        caretaker.redo()
        self.assertNotIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"), self.arr)
        caretaker.undo()
        self.assertIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"),self.arr)
        caretaker.backup()

if __name__ == "__main__":
    unittest.main()
