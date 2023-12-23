class Solution:
    def isPathCrossing(self, path: str) -> bool:
        history = set([(0, 0)])
        x, y = 0, 0
        
        for step in path:
            if step == 'N': y +=1
            elif step == 'S': y -=1
            elif step == 'W': x -=1
            elif step == 'E': x +=1
            if (x,y) in history: return True
            history.add((x,y))

        return False
