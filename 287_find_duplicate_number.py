#

# TODO: learning - slow/fast pointer does work here
#  Additional Ideas from the sol: Negative Marking(not meet constraint tho), "Array as Hashmap": Scooching each number at the place aof the
#  'number index' if it is already filled, it is duplicate
#  Best to just memorize the turtoise and hare solution
# Runtime: 660 ms, faster than 93.45% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 27.9 MB, less than 57.60% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break

        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


# Runtime: 635 ms, faster than 97.23% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 30.3 MB, less than 16.72% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set()
        for i in nums:
            if i in a:
                return i
            else:
                a.add(i)
