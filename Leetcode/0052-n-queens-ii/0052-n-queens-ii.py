class Solution:
    def totalNQueens(self, n: int) -> int:
        result_cnt = [0]
        def dfs(row, columns, diag_1, diag_2):
            if row==n:
                result_cnt[0] += 1
            else:
                for col in range(n):
                    if (
                        col not in columns 
                        and row-col not in diag_1
                        and row+col not in diag_2
                    ):
                        dfs(
                            row+1,
                            columns + [col],
                            diag_1 | {row-col}, 
                            diag_2 | {row+col}
                            )
        
        dfs(0, [], set(), set())
        return result_cnt[0]