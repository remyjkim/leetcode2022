# Runtime: 260 ms, faster than 88.18% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 73.17% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right: # use <= instead of <: this will allow else to take care of everything
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        # if nums[left] == target:
        #     return left
        return -1

    def search2(self, nums, target): # this answer related to prob 875: when we need to find the smallest number
        # that satisfies the condition
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) / 2
            if nums[m] > target:
                l = m + 1
            else: # Even it satisfies, we need to find the smallest number
                r = m
        return l