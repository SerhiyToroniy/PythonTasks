import copy

class Memento:
    def __init__(self, state: str, x) -> None:
        self._state = copy.deepcopy(state)
        self._x = copy.deepcopy(x)

    def get_state(self) -> str:
        return self._state

    def get_col(self):
        return self._x
