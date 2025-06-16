class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = -1
        l = float('inf')

        for num in nums:
            l = min(l, num)
            max_val = max(max_val, num - l)

        return max_val if max_val else -1
