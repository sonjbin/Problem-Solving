class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result_list = []
        def dfs(row, columns, diag_1, diag_2):
            if row == n:
                result_list.append(columns[:])
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
        output = []
        for q_idx in result_list:
            out = []
            for idx in q_idx:
                line = "." * idx + "Q" + "." * (n - idx - 1)
                out.append(line)
            output.append(out)
        return output