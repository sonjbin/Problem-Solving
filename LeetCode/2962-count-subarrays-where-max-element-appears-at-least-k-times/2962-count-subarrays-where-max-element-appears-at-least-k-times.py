class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        if nums.count(max_num) < k:
            return 0
        n = len(nums)
        left = 0
        cnt = 0
        answer = 0
        for right in range(n):
            if nums[right] == max_num:
                cnt += 1
            while cnt >= k:
                answer += n - right
                if nums[left] == max_num:
                    cnt -= 1
                left += 1
        
        return answer