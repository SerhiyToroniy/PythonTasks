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
        self.assertEqual(self.arr.search("Tor"),[SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17")])
        self.assertEqual(self.arr.search("Tor"),[SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17")])


        self.assertEqual(self.arr.search("seven"),[SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17")])
        self.assertEqual(self.arr.search("77777"),[SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17")])
        self.assertEqual(self.arr.search("UA77"),[SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17")])
        self.assertEqual(self.arr.search("2020.07.17"),[SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17")])

        self.assertEqual(self.arr.search("ivan"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])
        self.assertEqual(self.arr.search("67899"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])
        self.assertEqual(self.arr.search("8888"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])
        self.assertEqual(self.arr.search("2020.03.04"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])

        self.assertEqual(self.arr.search("eur"),[SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"),
                                                 SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"),
                                                 SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17")])

        self.assertNotEqual(self.arr.search("tor"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])
        self.assertNotEqual(self.arr.search("7777"),[SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04")])

    def test_sort(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        unCorrect.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))

        self.arr.sort("iban", self.arr)
        self.assertEqual(self.arr,temp)
        self.arr.sort("fee", self.arr)
        self.assertEqual(self.arr,unCorrect)
        self.arr.sort("currency", self.arr)
        self.assertEqual(self.arr,unCorrect)


    def test_delete(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        unCorrect.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))

        self.arr.delete_by_id("77777")
        self.assertEqual(self.arr,temp)
        self.assertNotIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"), self.arr)
        self.arr.delete_by_id("67899")
        self.assertNotIn(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"), self.arr)
        self.assertNotEqual(self.arr,unCorrect)

    def test_add(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        temp.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))
        temp.add(SwiftTransfer("55555", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

        self.arr.add_inputed(self.arr, SwiftTransfer("55555", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))
        self.assertIn(SwiftTransfer("55555", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"), self.arr)

        self.arr.add_inputed(self.arr, SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.assertIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"), self.arr)

        self.arr.add_inputed(self.arr, SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        self.assertIn(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"), self.arr)

        self.assertNotEqual(self.arr,unCorrect)

    def test_edit(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        temp.add(SwiftTransfer("77777", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

        self.arr.edit_by_id("77777", self.arr, SwiftTransfer("77777", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"))

        self.assertNotIn(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"),self.arr)
        self.assertIn(SwiftTransfer("77777", "UA55 5555 5555 5555", "Ivan Boyko", "5555.00", "uah", "555.00", "2020.05.15"),self.arr)

        self.assertEqual(self.arr,temp)
        self.assertNotEqual(self.arr,unCorrect)

    def test_undo(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        temp.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

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
        self.assertEqual(self.arr, temp)
        self.assertNotEqual(self.arr, unCorrect)

    def test_redo(self):
        temp = Collection()
        temp.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        temp.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))

        unCorrect = Collection()
        unCorrect.add(SwiftTransfer("68292", "UA21 3546 8231 9022", "Toroniy Serhiy", "20000.00", "eur", "500.00", "2020.09.17"))
        unCorrect.add(SwiftTransfer("67899", "UA88 8888 8888 8888", "Lomanow Ivan", "11000.00", "eur", "650.00", "2020.03.04"))
        unCorrect.add(SwiftTransfer("77777", "UA77 7777 7777 7777", "seven s", "7777.00", "eur", "777.00", "2020.07.17"))

        caretaker = Caretaker(self.arr)
        caretaker.backup()
        self.arr.delete_by_id("77777")
        caretaker.backup()
        caretaker.undo()
        caretaker.redo()
        caretaker.undo()
        caretaker.redo()
        self.assertEqual(self.arr, temp)
        caretaker.undo()
        self.arr.sort("currency",self.arr)
        caretaker.backup()
        self.assertEqual(self.arr, unCorrect)

if __name__ == "__main__":
    unittest.main()