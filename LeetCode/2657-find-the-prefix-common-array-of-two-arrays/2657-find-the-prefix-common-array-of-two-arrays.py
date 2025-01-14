class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * (n+1)
        cnt = [0] * (n+1)
        for i in range(n):
            a, b = A[i], B[i]
            new = 0
            cnt[a] += 1
            if cnt[a] == 2:
                new += 1
            cnt[b] += 1
            if cnt[b] == 2:
                new += 1
            
            result[i+1] = result[i] + new
    
        return result[1:]