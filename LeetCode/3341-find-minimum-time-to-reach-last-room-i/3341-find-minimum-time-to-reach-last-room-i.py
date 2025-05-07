class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        visited = [[False]*m for _ in range(n)]
        heap = [(0,0,0)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n-1 and y == m-1:
                return time
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    next_time = max(time, moveTime[nx][ny]) + 1
                    heapq.heappush(heap, (next_time, nx, ny))
            

        