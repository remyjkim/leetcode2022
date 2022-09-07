# Runtime: 50 ms, faster than 80.87% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.2 MB, less than 90.92% of Python3 online submissions for Search in Rotated Sorted Array.
# TODO: learning - conding two binary search is still O(logn!!!)
#  Choose carefully how to choose the pivot, and how to utilize the pivot to decide which way to go
#  If possible, use nums[-1] or nums[0] for comparison

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l= m + 1
            else:
                r= m
        pivot = l
        # print(pivot)

        # compare target with the last element, and think carefully about whether to insert equal sign here
        if nums[-1] < target:
            l, r = 0, pivot-1
        else:
            l, r = pivot, len(nums) -1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l= m + 1
            else:
                r= m
        # print(l)
        if nums[l] == target:
            return l
        return -1