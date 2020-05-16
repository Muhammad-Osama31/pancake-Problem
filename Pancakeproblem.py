
from searchProblem import SearchProblem
import copy
from pancakestate import Pancakestate
class Pancakeproblem:
   
    def __init__(self,initialState,goalState):
    self._initialState = Pancakestate(initialState, '', 0)
    self._goalState = _goalState
    self._numberOfColumns = len(initialState[0])
	
   def initialState(self):
   return self._initialState
   def succesorFunction(self,cs):
   nextMoves = []
   emptyColumn = 0
   currentState = cs.currentState
   emptyFound = False

   def succesorFunction(self,cs):
   nextMoves = []
   emptyColumn = 0,0
   currentState = cs.currentState
   emptyFound = False
   for i in range(len(currentState)):
   if currentState[i] == 0:
   emptyColumn = i
   emptyFound = True
   break
   if emptyFound:
   break

  if emptyColumn != 0:
    newState = copy.deepcopy(currentState)
    tempS = newState[emptyColumn-1]
    newState[emptyColumn-1] = 0
    newState[emptyColumn] = tempS 
    pc= Pancakestate(newState, 'Move Left', 1.0)
    nextMoves.append(pc)

  if emptyColumn +1 != self._numberOfColumns:
    newState = copy.deepcopy(currentState)
    tempS = newState[emptyColumn+1]
    newState[emptyColumn+1] = 0
    newState[emptyColumn] = tempS
    pc= EightPuzzleState(newState, 'Move Right', 1.0)
    nextMoves.append(pc)
    return nextMoves

    def isGoal(self,currentState):
    cs = currentState.getCurrentState()
    for i in range(len(cs)):
    if cs[i]!= self._goalState[i]:
        return False
    return True












