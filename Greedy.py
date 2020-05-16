from heuristic import heuristic 
from node import Node
class Greedy(SearchStrategy):

def __init__(self, heuristic):

self.heuristic = heuristic
self.queue = PriorityQueue()
def isEmpty(self):
return self.queue == []


def addNode(self,node):
self.queue.put((self.heuristic.evaluateNode(node.state.currentState),node))
def removeNode(self):
return self.queue.get()[1]
   
    def evaluateNode(self,state):
    totalCost = 0
    for i in range(len(state)):
        if state[i] != self.goal[i]:
        totalCost += 1
    return totalCost

   