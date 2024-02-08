class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        two_posts_back = k
        one_post_back = k * k
3
