

# TODO: learning - Quick Select, kind of doing binary search towards the kth point while also doing some sort of
#  quick sort at every iteration - involves pivoting
#   This takes (on average) O(log n) iterations with the cost of each iteration being roughly half of the previous one),
#   which alludes to a geomtric series that converges to linear run-time.
#  Using heap would make this O(NlogK)

class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return

        pivot = random.choice(nums)

        greaterThanPivot = [x for x in nums if x > pivot]
        equalToPivot = [x for x in nums if x == pivot]
        lessThanPivot = [x for x in nums if x < pivot]

        greaterLength = len(greaterThanPivot)
        equalLength = len(equalToPivot)

        if k <= greaterLength:
            return self.findKthLargest(greaterThanPivot, k)
        elif k > greaterLength + equalLength:
            return self.findKthLargest(lessThanPivot, k - greaterLength - equalLength)
        else:
            return equalToPivot[0]