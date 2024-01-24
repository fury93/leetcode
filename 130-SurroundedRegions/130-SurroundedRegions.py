from itertools import product
class Solution(object):
    def solve(self, board):
        R, C = len(board), len(board[0])
        if R < 3 or C < 3: return 
        
        def dfs(board, x, y):
            if 0 <= x < R and 0 <= y < C and board[x][y] == 'O':
                board[x][y] = '.'
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    dfs(board, x + dx, y + dy)
        
        for x, y in chain(product([0, R-1], range(C)), product(range(R), [0, C-1]))
:
            dfs(board, x, y) 
                 
        for x, y in product(range(R), range(C)):
            if board[x][y] == 'O':
                board[x][y] = 'X'
            elif board[x][y] == '.':
                board[x][y] = 'O'
                
    
[
