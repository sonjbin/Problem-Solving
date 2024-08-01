class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            k = (r+l)//2
            if sum([math.ceil(x/k) for x in piles]) <= h:
                r = k
            else:
                l = k+1
        
        return l

