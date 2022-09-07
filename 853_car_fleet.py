# Used the solution
# TODO: learning - 1) visualize well 2) Test out 3 cases at least
#  3) Think carefully which way we should do the search samllest to biggest? or vice versa?

# Runtime: 889 ms, faster than 99.53% of Python3 online submissions for Car Fleet.
# Memory Usage: 36.8 MB, less than 24.89% of Python3 online submissions for Car Fleet.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target-p)/s for p,s in sorted(zip(position, speed))]
        slowest = 0
        fleet = 0
        for t in time[::-1]:
            if slowest < t:
                fleet +=1
                slowest = t
        return fleet