# Shorter Version with using 0
def lastStoneWeight(self, A):
    h = [-x for x in A]
    heapq.heapify(h)
    while len(h) > 1 and h[0] != 0:
        heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
    return -h[0]

# Runtime: 63 ms, faster than 20.70% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.7 MB, less than 99.73% of Python3 online submissions for Last Stone Weight.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-1*i for i in stones]
        heapq.heapify(self.heap)
        while len(self.heap) >1:
            large = heapq.heappop(self.heap)
            small = heapq.heappop(self.heap)
            if large != small:
                heapq.heappush(self.heap, large-small)
        if self.heap:
            return -self.heap[0]
        else:
            return 0