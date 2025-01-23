class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        hash_row = {}
        hash_col = {}

        server_id = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i not in hash_row:
                        hash_row[i] = set()
                    hash_row[i].add(server_id)
                    if j not in hash_col:
                        hash_col[j] = set()
                    hash_col[j].add(server_id)
                    server_id += 1

        result = list(hash_row.values()) + list(hash_col.values())

        connected = []
        for group in result:
            if len(group) > 1:
                connected += group
        
        return len(set(connected))