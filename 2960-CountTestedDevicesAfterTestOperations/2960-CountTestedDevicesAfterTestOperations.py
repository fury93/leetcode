class Solution:
    def countTestedDevices(self, p: List[int]) 
-> int:
        tested = 0
        for i in range(len(p)):
            if p[i] > tested:
                tested += 1
        return tested

                


        
