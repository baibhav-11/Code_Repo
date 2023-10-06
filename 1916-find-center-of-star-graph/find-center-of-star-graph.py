class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = [0] * (len(edges) + 2)  # Initialize degree list
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        max_degree_node = degree.index(max(degree))
        
        return max_degree_node