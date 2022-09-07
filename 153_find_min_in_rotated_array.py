# Runtime: 50 ms, faster than 79.80% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.1 MB, less than 63.50% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l= m + 1
            else:
                r= m
        return nums[l]