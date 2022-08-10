# Runtime: 104 ms, faster than 16.22% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.2 MB, less than 11.53% of Python3 online submissions for Valid Anagram.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        sorted_nums = sorted(nums)
        for i in range(length-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False


# Runtime: 62 ms, faster than 73.44% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 66.69% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s)==Counter(t)