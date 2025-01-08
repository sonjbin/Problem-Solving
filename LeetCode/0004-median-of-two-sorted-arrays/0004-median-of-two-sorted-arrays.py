class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        l, r = 0, x
        half_len = (x+y+1)//2
        while l<=r:
            partition_1 = (l+r)//2
            partition_2 = half_len - partition_1

            max_left_1 = float('-inf') if partition_1 == 0 else nums1[partition_1 - 1]
            min_right_1 = float('inf') if partition_1 == x else nums1[partition_1]
            max_left_2 = float('-inf') if partition_2 == 0 else nums2[partition_2 - 1]
            min_right_2 = float('inf') if partition_2 == y else nums2[partition_2]

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (x+y)%2 == 0:
                    return (max(max_left_1, max_left_2)+min(min_right_1, min_right_2))/2
                else:
                    return max(max_left_1, max_left_2)
            
            if max_left_1 > min_right_2:
                r = partition_1 - 1
            else:
                l = partition_1 + 1
