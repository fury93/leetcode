            graph[u].add(v)
            u, v = edge
        for edge in edges:
        graph = [set() for i in range(len(edges)+1)]
    def treeDiameter(self, edges: List[List[int]]) -> int:
class Solution:
            graph[v].add(u)

        diameter = 0

        def dfs(curr, visited):
            nonlocal diameter
            top_1_distance, top_2_distance = 0, 0
            distance = 0
            visited[curr] = True

            for neighbor in graph[curr]:
[
