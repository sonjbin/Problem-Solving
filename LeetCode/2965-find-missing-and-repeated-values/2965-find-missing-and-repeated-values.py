class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt_list = [-1] + [0] * n*n
        for i in range(n):
            for j in range(n):
                cnt_list[grid[i][j]] += 1
        
        ans = [cnt_list.index(2), cnt_list.index(0)]
        return ans