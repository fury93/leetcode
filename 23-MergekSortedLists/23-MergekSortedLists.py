[
class Solution:
    def findCircleNum(self, A):
        
        def dfs(node):
            for city, isConnected in enumerate(A[node]):
                if isConnected and city not in seen:
                    seen.add(city)
                    dfs(city)
        
        ans, seen = 0, set()
        for city in range(len(A)):
            if city not in seen:
                dfs(city)
                ans += 1
        return ans
