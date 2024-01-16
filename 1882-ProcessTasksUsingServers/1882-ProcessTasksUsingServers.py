class Solution:
    def assignTasks(self, servers: List[int], tasks: List
[int]) -> List[int]:
        res, unavailable, time = [], [], 0
        available = [(weight, id) for id, weight in 
enumerate(servers)]
        heapify(available)
[
