class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[-1] = 1
        for i in range(len(nums)-1, -1, -1):
            max_seq = None
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if not max_seq or dp[j] > max_seq:
                        max_seq = dp[j]
            if max_seq:
                dp[i] = max_seq + 1
        return max(dp)