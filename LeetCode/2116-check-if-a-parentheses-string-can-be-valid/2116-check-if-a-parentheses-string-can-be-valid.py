class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        open_min = open_max = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_max += 1
            else:
                open_max -= 1
            
            if s[i] == ')' or locked[i] == '0':
                open_min -= 1
            else:
                open_min += 1
            
            if open_max < 0:
                return False
            open_min = max(0, open_min)

        return open_min == 0
