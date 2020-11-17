from Iterator import *
from Validation import *
from Strategy import *
from Logger import *
from Event import *
import copy

class ConcreteStrategyIterator(Strategy):

    @staticmethod
    @Validation.index_check
    @Validation.limit_check
    def insert(lst, limit, index):
        limit = int(limit)
        newLst = []
        save_index = copy.copy(index)
        for i in MyIterator(limit):
            newLst.append(i)
            lst.insert(index, i)
            index+=1
        e = Event()
        e.run("add(ListIterator)", save_index, newLst, lst)