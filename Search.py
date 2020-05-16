from node import Node
from pancakeProblem import PancakeProblem

class Search:

    def fliping(int visitedNode[], int i): 
           i=len(visitednode)
        int tempor,initials=0
        while initials < i : 
            tempor = visitedNode[initials] 
            visitedNode[initials] = visitedNode[i] 
            visitedNode[i] = tempor; 
            initials++ 
            i--
        } 
    } 
  
  
    def SearchMax(int visitedNode[], int n): 
        Mins=0
        i=0 
        while  i < n: 
            if visitedNode[i] > visitedNode[mins]: 
                vistedNode[mins] = vistedNode[i]
		        i++ 
        return mi 
     
  
     
    def pancakeSolve(int visitedNode[], int n): 
    
         curr_size = (int) n
         while curr_size > 1: 
            
            int mins = SearchMax(visitedNode[mins], curr_size); 
            if (mins != curr_size - 1): 
                fliping(visitedNode, mins); 
                flipping(visitedNode, curr_size - 1) 
        
         return 0; 
         --curr_size 
  
  
    def solvedCakeprinting(int visitedNode[], int Node_size): 
	int i = 0        
        while i < Node_size: 
            print(visitedNode[i] + " ") 
            print("\n") 
    	    i++