# Runtime: 497 ms, faster than 26.59% of Python3 online submissions for Permutation in String.
# Memory Usage: 14 MB, less than 31.61% of Python3 online submissions for Permutation in String.

# TODO: this is an optimized version of sliding window that tracks whether the changes entries just became zero or not.
#  this one is from discussions, and needs review
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr:
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True

        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        if len(count1-count2) is 0:
                return True
        for i in range(len(s1), len(s2)):
            count2[s2[i-len(s1)]]-=1
            count2[s2[i]]+=1
            if len(count1-count2) is 0:
                return True
        return False