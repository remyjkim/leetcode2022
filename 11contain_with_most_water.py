#TODO: Why is advancing two pointer work here?
# Is this search really exhaustive?
#Had to use Solution
#Runtime: 810 ms, faster than 87.94% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 12.77% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = min(height[left], height[right])*right
        while(left < right):
            width = right-left
            maxArea = max(maxArea, min(height[left], height[right])*width)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return maxArea