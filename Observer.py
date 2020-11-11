class Observer:
    _D = dict()

    def attach(self, state, method):
        self._D[state] = method

    def getDictionary(self):
        return self._D