class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1 :
            return nums
        elif len(nums) == 2:
            return [min(nums), max(nums)]
        center_idx = len(nums)//2
        left = self.sortArray(nums[:center_idx])
        right = self.sortArray(nums[center_idx:])
        result = []
        l, r = 0, 0
        while l < len(left) or r < len(right):
            if l >= len(left) or (r < len(right) and left[l] >= right[r]):
                result.append(right[r])
                r += 1
            else:
                result.append(left[l])
                l += 1
        return result
