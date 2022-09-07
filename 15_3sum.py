# Used the solution
# Another two pointer questions: to keep the target sum, we need to advance either from the left or right
# (assuming that the list is sorted)
# Runtime: 671 ms, faster than 97.04% of Python3 online submissions for 3Sum.
# Memory Usage: 18.1 MB, less than 39.41% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
            # print(i, "th:", res)
        return res

    def twoSum(self, numbers: List[int], i: int, res: List[List[int]]):
        left = i + 1
        right = len(numbers) - 1
        while (left < right):
            sum = numbers[left] + numbers[right]
            if sum < -numbers[i]:
                left += 1
            elif sum > -numbers[i]:
                right -= 1
                # left = 0 #
            else:
                res.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1  # They're both obsolete, need to move on with both
                while left < right and numbers[left - 1] == numbers[left]:
                    left += 1  # at least one of left or right need to change from previous
