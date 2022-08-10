# Runtime: 655 ms, faster than 34.44% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 77.11% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _nums = sorted(nums)
        for i, n in enumerate(_nums):
            if target-n in _nums[i+1:]:
                if target-n == n:
                    r = nums.index(n)
                    return [r, nums.index(target-n,r+1)]
                else:
                    return [nums.index(n), nums.index(target-n)]
            else:
                continue

#Using Hashmaps
#Runtime: 108 ms, faster than 55.34% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.50% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            if target-n in hashmap:
                return [i, hashmap[target-n]]
            hashmap[n] = i