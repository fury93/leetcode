        for j, i in product(range(C), range(R)):
            maxCol[j] = max(maxCol[j], matrix[i][j])

        for i, j in product(range(R), range(C)):
            if matrix[i][j] == -1:
                matrix[i][j] = maxCol[j]

        
        R, C = len(matrix), len(matrix[0])
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
class Solution:
        maxCol = [-1] * C
        return matrix

[
