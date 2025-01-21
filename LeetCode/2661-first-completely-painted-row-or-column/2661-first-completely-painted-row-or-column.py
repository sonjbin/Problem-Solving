class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_cnt = m * [n]
        col_cnt = n * [m]

        position_dict = {mat[i][j]:(i, j) for j in range(n) for i in range(m)}

        for pos, k in enumerate(arr):
            i, j = position_dict[k]
            row_cnt[i] -= 1
            col_cnt[j] -= 1
            if row_cnt[i] == 0 or col_cnt[j] == 0:
                return pos
        return -1