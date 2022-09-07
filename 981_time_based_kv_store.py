# Runtime: 1669 ms, faster than 8.23% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 72.4 MB, less than 31.31% of Python3 online submissions for Time Based Key-Value Store.
# TODO: memorize to use bisect.bisect -> gives the position in which to insert the new value

class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append([timestamp, value])
        # print(self.kv[key])

    # TODO: learning - this is the fastest
    # Runtime: 1216 ms, faster than 40.28% of Python3 online submissions for Time Based Key-Value Store.
    # Memory Usage: 67.5 MB, less than 99.26% of Python3 online submissions for Time Based Key-Value Store.
    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''

    # TODO: learning - this is a better version
    #  1) return right-1 entry instead of right
    #  2) left == 0 means there is no entry to return
    def get(self, key, timestamp):
        arr = self.kv[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid

        return "" if left == 0 else arr[right - 1][1]

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.kv[key]) - 1
        if not self.kv[key] or self.kv[key][0][0] > timestamp:
            return ""
        while l < r:
            m = (l + r) // 2
            # print(f"comparing {self.kv[key][m][0]} with {timestamp}")
            if self.kv[key][m][0] > timestamp:  # careful with this inequality
                r = m
            else:
                l = m + 1
        return self.kv[key][l - 1][1]
