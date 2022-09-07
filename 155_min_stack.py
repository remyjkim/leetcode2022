# Runtime: 76 ms, faster than 76.90% of Python3 online submissions for Min Stack.
# Memory Usage: 17.8 MB, less than 96.01% of Python3 online submissions for Min Stack.

# used the solution for the two stack case
# TODO: learning - always do 3 cases with drawings.
#  cover carefully the pop, push cases and how to manipulate them
#  and always think about the the case where the data structure could be empty

class MinStack:

    def __init__(self):
        self.a = []
        self.min = []

    def push(self, val: int) -> None:
        self.a.append(val)
        # if self.min is empty, just add the value
        # if val is smaller, append it
        if not self.min or self.min[-1][0] > val:
            self.min.append([val, 1])
            # if val is in the min stack, increment the count
        elif val == self.min[-1][0]:
            self.min[-1][1] +=1

    def pop(self) -> None:
        res = self.a.pop()
        if res == self.min[-1][0]:
            self.min[-1][1] -= 1
        if not self.min[-1][1]:
            self.min.pop()
        return res

    def top(self) -> int:
        if len(self.a)!=0:
            return self.a[-1]
        else:
            return None

    def getMin(self) -> int:
        # print(self.min)
        if not self.min:
            return None
        else:
            return self.min[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Runtime: 125 ms, faster than 20.86% of Python3 online submissions for Min Stack.
# Memory Usage: 17.8 MB, less than 79.17% of Python3 online submissions for Min Stack.

class MinStack:

    def __init__(self):
        self.a = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.a.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        res = self.a.pop()
        self.min = min(self.a) if len(self.a) != 0 else float("inf")
        return res

    def top(self) -> int:
        if len(self.a)!=0:
            return self.a[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.min == float("inf"):
            return None
        else:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()