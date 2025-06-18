class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        n = len(nums)
        while r < n-1:
            max_jump = 0
            for i in range(l, r+1):
                max_jump = max(max_jump, nums[i] + i)
            l = r+1
            r = max_jump
            res += 1
        
        return res
