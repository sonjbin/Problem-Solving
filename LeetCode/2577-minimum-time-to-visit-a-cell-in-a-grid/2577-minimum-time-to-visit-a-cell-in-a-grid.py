class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        min_time = [[float('inf')] * n for _ in range(m)]
        heap = [(0, 0, 0)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (m-1, n-1):
                return time
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    next_time = max(time + 1, grid[nx][ny])
                    if (time - next_time) % 2 == 0:
                        next_time += 1
                    if next_time < min_time[nx][ny]:
                        min_time[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))