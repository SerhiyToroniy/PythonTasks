from Iterator import *
from Validation import *
from Strategy import *

class ConcreteStrategyIterator(Strategy):

    @staticmethod
    @Validation.index_check
    @Validation.limit_check
    def insert(lst, limit, index):
        limit = int(limit)
        for i in MyIterator(limit):
            lst.insert(index, i)
            index+=1