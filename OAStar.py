from node import Node
from pancakeproblem import PancakeProblem
from greedy import Greedy
from ucs import UCS
from heuristic import heuristic

class AStar:

       def AStar(Node nodes, Node goal):

        source.pathCost = 0
        PriorityQueue<Node> queue = new PriorityQueue<Node>(20,new Comparator<Node>():

            def compare(Node i, Node j):
                if(i.pathCost > j.pathCost):
                    return 1

                 else if (i.pathCost < j.pathCost):
                     return -1
                 else:
                     return 0
          
    
        queue.add(source)
        Set<Node> explored = new HashSet<Node>()
        boolean found = false

    def evaluateNode(self,state):
    totalCost = 0
    for i in range(len(state)):
        if state[i] != self.goal[i]:
        totalCost += 1
    return totalCost




class Edge:
    double cost
    Node target

    def Edge(Node targetNode, double costVal):
        cost = costVal
        target = targetNode

