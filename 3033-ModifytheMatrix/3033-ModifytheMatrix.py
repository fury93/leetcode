
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        
            for i in range(R):
                maxColVal = max(maxColVal, matrix[i][j])
        for j in range(C):
            maxColVal = -1
            for i in range(R):
                if matrix[i][j] == -1:
                    matrix[i][j] = maxColVal 
            
        return matrix

[
