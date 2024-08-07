class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k%len(nums)
        def reverse_inplace(nums, n, m):
            for i in range((m-n+1)//2):
                temp = nums[m-i]
                nums[m-i] = nums[n+i]
                nums[n+i] = temp

        reverse_inplace(nums, 0, len(nums)-k-1)
        reverse_inplace(nums, len(nums)-k, len(nums)-1)
        nums.reverse()

