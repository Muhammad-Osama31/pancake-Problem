from node import Node
from pancakeproblem import PancakeProblem

class UCS:

       def UCSearch(Node nodes, Node goal):

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

       
        do:

            Node current = queue.poll()
            explored.add(current)


            if(current.value.equals(goal.value)):
                found = true





            for(Edge e: current.adjacencies):
                Node child = e.target
                double cost = e.cost
                child.pathCost = current.pathCost + cost


                if(!explored.contains(child) && !queue.contains(child)):

                    child.parent = current
                    queue.add(child)
                    System.out.println(child)
                    System.out.println(queue)
                    System.out.println()


                else if((queue.contains(child))&&(child.pathCost>current.pathCost)):

                    child.parent=current
                    current = child

                


while(!queue.isEmpty()):pass



class Edge:
    double cost
    Node target

    def Edge(Node targetNode, double costVal):
        cost = costVal
        target = targetNode

