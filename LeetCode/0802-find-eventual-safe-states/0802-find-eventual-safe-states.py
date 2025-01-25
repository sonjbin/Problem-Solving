class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        states = [0] * n # 0: not visited, 1: visiting, 2: safe

        def dfs(node):
            if states[node] != 0:
                return states[node] == 2
            
            states[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            states[node] = 2
            
            return True
        
        return [node for node in range(n) if dfs(node)]
