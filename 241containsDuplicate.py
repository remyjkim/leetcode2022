"""Given an integer array nums, return true if
any value appears at least twice in the array,
and return false if every element is distinct.
"""


# Runtime: 632 ms, faster than 56.08% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.9 MB, less than 72.31% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

# Runtime: 585 ms, faster than 65.75% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 5.09% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        sorted_nums = sorted(nums)
        for i in range(length-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False