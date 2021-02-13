from Strategy import *

class Contex:
    def __init__(self, strat: Strategy = None):
        self.strategy = strat

    def setStrategy(self, strat: Strategy):
        self.strategy = strat

    def getStrategy(self):
        return self.strategy

    def execudeStrategy(self,lst, var = None, index = None):
        return self.strategy.insert(lst, var, index)