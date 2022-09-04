# Runtime: 691 ms, faster than 45.46% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 28.9 MB, less than 46.95% of Python3 online submissions for Longest Consecutive Sequence.
# The crux here is to use HashSet to make searching O(1) and keep on using that to search for the longest streaks

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                j = i+1
                while j in nums:
                    j+=1
                longest = max(longest, j-i)
        return longest