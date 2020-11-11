from Observer import *

class Event:

    @staticmethod
    def run(state = None, pos = None, new = None, result = None):
        for i in Observer().getDictionary():
            if i == state:
                Observer().getDictionary()[i](state,pos,new,result)