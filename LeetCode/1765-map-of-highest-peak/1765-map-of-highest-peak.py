class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[None]*n for _ in range(m)]

        deq = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    heights[i][j] = 0
                    deq.append((i, j))
        
        while deq:
            i, j = deq.popleft()
            h = heights[i][j] + 1
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n and heights[r][c] is None: 
                    heights[r][c] = h
                    deq.append((r,c))
        
        return heights
                    
                    
                    
                    
                    
            