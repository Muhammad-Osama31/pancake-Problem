if __name__ =='__main__':
    
# 0,8,7,6,5,4,3,2,1
goal = [0,1,2,4,5,6,7,8,9,10,11,12]
heuristic = Greedy(goal)
searchProblem = pankcakeproblem([10,9,4,6,3,7,12,11,,8,5,3,2,1], goal)
searchStrategy = GreedySearch(heuristic)
search = Search(searchProblem, searchStrategy)
result = search.solveProblem()
if result is not None:
search.printResult(result)
    
   
    
        
          
        

