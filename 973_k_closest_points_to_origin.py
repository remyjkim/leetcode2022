# Runtime: 1028 ms, faster than 74.93% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.3 MB, less than 81.26% of Python3 online submissions for K Closest Points to Origin.
# TODO: learning - use heapq.nsmallest, lambda as the third parameter
#  memorize the heapq.nsmallest parameters
class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0]**2 + x[1]**2)

# Runtime: 1961 ms, faster than 12.89% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.4 MB, less than 61.77% of Python3 online submissions for K Closest Points to Origin.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myheap = [(point[0]**2+point[1]**2, point) for point in points]
        heapq.heapify(myheap)
        return [heapq.heappop(myheap)[1] for i in range(k)]