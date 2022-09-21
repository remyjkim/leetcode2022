# Runtime: 201 ms, faster than 31.01% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.1 MB, less than 62.83% of Python3 online submissions for Kth Largest Element in a Stream.
# TODO: learning - learn to use heapq.heapify, heapq.heappop, heapq.heappush, heapq.heapreplace

class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val) #pops the smallest one and pushes in the new
        return self.pool[0]


# Runtime: 2515 ms, faster than 5.00% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.4 MB, less than 24.55% of Python3 online submissions for Kth Largest Element in a Stream.

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) >= k:
            self.topk = sorted(nums)[-self.k:]
        else:
            self.topk = sorted(nums)

    def add(self, val: int) -> int:
        self.topk = sorted(self.topk + [val])[-self.k:]
        return self.topk[0]