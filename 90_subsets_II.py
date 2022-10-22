# Runtime: 80 ms, faster than 17.68% of Python3 online submissions for Subsets II.
# Memory Usage: 14 MB, less than 93.91% of Python3 online submissions for Subsets II.
# TODO: MAKE SURE TO REVIEW THIS QUESTION!!!! It all comes down to how to react differently when encountered with seen vs. unseen
# TODO: learning - keep track of two arrays: 1) if not a duplicate elem, we duplicate the whole res by just adding elem
#  at the end and also use it as new cur; 2) if it is a duplicate, we doulbe cur by adding the duplicate elem.
#  cur keeps the non-empty power set with at least one newest elem
# TODO: backtracking - proceed(another backtracking with next index) if not duplicate, do not if it isn't
#  under this scheme, new results should be added as you go along


# Backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, curSubset):
            ans.append(curSubset[::])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]: continue  # Skip duplicates
                curSubset.append(nums[i])
                backtrack(i + 1, curSubset)
                curSubset.pop()

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans

# Iterative solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return
        res = [[]]
        cur = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                cur = [item+[nums[i]] for item in cur]
            else:
                cur = [item+[nums[i]] for item in res]
            res += cur
            # print(cur, "/",res)
        return res



class Solution(object):
    def subsetsWithDup(self, nums):
        nums, result, pos = sorted(nums), [[]], {}
        for n in nums:
            # pos.get will output 0 if unseen, if seen, it will give you the position already seen
            start, l = pos.get(n, 0), len(result)
            result += [r + [n] for r in result[start:]]
            pos[n] = l
        return result