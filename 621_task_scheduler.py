# Runtime: 695 ms, faster than 67.39% of Python3 online submissions for Task Scheduler.
# Memory Usage: 14.3 MB, less than 91.40% of Python3 online submissions for Task Scheduler.
# TODO: learning - think when there has to be any idle! if that doesn't happen, it'll just be the length of the tasks!
#  always think about using max functions instead of if statements

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counted = list(collections.Counter(tasks).values())
        max_n = max(counted)
        mct = counted.count(max_n)
        return max(len(tasks), (max_n-1)*(n+1)+mct)
