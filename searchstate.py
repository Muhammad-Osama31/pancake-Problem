from abc import abstractmethod

class SearchState(object):

@abstractmethod
def __init__(self, params): pass
@abstractmethod
def getCurrentState(self): pass
@abstractmethod
def getAction(self): pass
@abstractmethod
def getCost(self):pass
@abstractmethod
def getHeuristicValue():pass
@abstractmethod
def stringRep(self) : pass


