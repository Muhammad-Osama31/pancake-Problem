class Heuristic(object):
    
@abstractclassmethod
def __init__(self): pass
@abstractclassmethod
def evaluateNode(self,state,goal): pass