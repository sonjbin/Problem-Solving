class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s) <= numRows:
            return s
        row_chars = [''] * numRows
        direction = 1
        row_idx = 0
        for c in s:
            row_chars[row_idx] += c
            if row_idx == 0:
                direction = 1
            elif row_idx == numRows-1:
                direction = -1
            row_idx += direction
        
        return ''.join(row_chars)
                
