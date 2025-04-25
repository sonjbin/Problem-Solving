class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        n = len(nums)
        cnt = 0
        l = 0
        unique = 0
        freq = defaultdict(int)
        for r in range(n):
            freq[nums[r]] += 1
            if freq[nums[r]] == 1:
                unique += 1
                while unique == total_unique:
                    cnt += n-r
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        unique -= 1
                    l += 1
                
        return cnt