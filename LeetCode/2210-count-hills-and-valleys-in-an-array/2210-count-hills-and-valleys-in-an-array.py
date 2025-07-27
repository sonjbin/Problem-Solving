class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt=0
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] == nums[i-1]:
                continue
            lh, lv, rh, rv = 0, 0, 0, 0
            curr = nums[i]
            # left
            for l in range(i-1, -1, -1):
                if nums[l] < curr:
                    lh = 1
                    break
                if nums[l] > curr:
                    lv = 1
                    break
            # right
            for r in range(i+1, n):
                if nums[r] < curr:
                    rh = 1
                    break
                if nums[r] > curr:
                    rv = 1
                    break
            cnt += lh * rh + lv * rv

        return cnt
