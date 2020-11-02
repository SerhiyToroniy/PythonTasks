from Memento import *

class Caretaker:
    _max_size = 0
    _undo_count = 0
    _redo_count = 0

    def __init__(self, originator):
        self._mementos = []
        self._originator = originator
        self._position = -1

    def backup(self) -> None:
        if self._max_size > 5:
            print("You can remember only 5 actions! Your last action is not remembered.")
            self._mementos.remove(self._mementos[0])
            return
        self._max_size += 1
        self._mementos.insert(self._position+1, self._originator.save())
        self._position += 1
        self._undo_count = 0
        self._redo_count = 0

    def undo(self) -> None:
        self._undo_count += 1
        if not len(self._mementos) or self._position <= 0:
            print("You can't use undo!")
            return
        self._position -= 1
        memento = self._mementos[self._position]
        self._originator.restore(memento)

    def redo(self) -> None:
        self._redo_count += 1
        if not len(self._mementos) or self._position == len(self._mementos)-1 or self._redo_count > self._undo_count:
            print("You can't use redo!")
            return
        self._position += 1
        memento = self._mementos[self._position]
        self._originator.restore(memento)