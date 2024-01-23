class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) 
-> bool:
        R, C = len(matrix), len(matrix[0])
        for row in range(1, R):
            for col in range(1, C):
                if matrix[row][col] != matrix[row-1]
[col-1]: return False
        return True
