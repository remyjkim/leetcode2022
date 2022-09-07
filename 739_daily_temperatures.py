# Used the solution
# TODO: learning -  1. looking from backward: but need to keep track of right_max and make it so that consequent #'s are 0
#  2. Using the while loop that changes how many steps we're gonna advance
#  3. If a>b, b<c, then a is never resolved until a number bigger than b emerge!!
# Runtime: 1194 ms, faster than 97.74% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 26 MB, less than 6.64% of Python3 online submissions for Daily Temperatures.


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float('-inf')
        res = [0] * n
        for i in range(n-1, -1, -1):
            t = T[i]
            if right_max <= t:
                right_max = t
            else:
                days = 1
                while T[i+days] <= t:
                    days += res[i+days]
                res[i] = days
        return res

# TODO: learning - if the a>b, b<c, then a is never resolved until
#  a number bigger than b emerges -> stack usage!!
class Solution:
    def dailyTemperatures(self, T):

        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
          while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
          stack.append(i)
        return ans