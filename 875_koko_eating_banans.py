# Runtime: 785 ms, faster than 38.34% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15.5 MB, less than 74.69% of Python3 online submissions for Koko Eating Bananas.

# TODO: learning: when binary searching, need to think carefully on the equal signs(you could use them or not use them)
#  You can also use the equal sign to make the search go til the end to the most optimal answer

class Solution:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) / 2
            if sum((p + m - 1) / m for p in piles) > H:
                l = m + 1
            else:
                r = m
        return l
