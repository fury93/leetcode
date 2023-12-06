[
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [[i, v] for i, v in 
enumerate(nums) if v != 0]

    # Return the dotProduct of two sparse 
vectors
    def dotProduct(self, vec: 
'SparseVector') -> int:
        res, i, j, n1, n2 = 0, 0, 0, self.
nums, vec.nums
        while i < len(n1) and j < len(n2):
            if n1[i][0] == n2[j][0]:
                res += n1[i][1] * n2[j][1]
                i += 1
                j += 1
            elif n1[i][0] < n2[j][0]:
