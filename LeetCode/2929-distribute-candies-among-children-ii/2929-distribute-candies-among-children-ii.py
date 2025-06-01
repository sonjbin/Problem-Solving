class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_total_ways(n):
            return comb(n + 2, 2) if n >= 0 else 0
        
        total = count_total_ways(n)
        over1 = count_total_ways(n - (limit + 1)) * 3
        over2 = count_total_ways(n - 2 * (limit + 1)) * 3
        over3 = count_total_ways(n - 3 * (limit + 1))

        return total - over1 + over2 - over3