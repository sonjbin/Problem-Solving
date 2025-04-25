class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1  
        prefix_sum = 0
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix_sum += 1
            target = (prefix_sum-k) % modulo
            result += count_map[target]

            count_map[prefix_sum%modulo] += 1
        
        return result