#Used solution

#best solution: with two pointers
# when there is max or min operation between the left end and the right end involved -> think about two pointers
#Runtime: 143 ms, faster than 86.90% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.9 MB, less than 96.06% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_surf = height[0]
        right_surf = height[-1]
        sum = 0
        while(left<right):
            if height[left] < height[right]:
                left+=1
                if height[left] < left_surf:
                    sum += left_surf - height[left]
                else:
                    left_surf = height[left]
            else:
                right-=1
                if height[right] < right_surf:
                    sum += right_surf - height[right]
                else:
                    right_surf = height[right]
        return sum






#this one with left search and right search combined -> dynamic programming
#Runtime: 355 ms, faster than 5.00% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 16.1 MB, less than 44.81% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        current_surf = 0
        for i, n  in enumerate(height):
            if n > current_surf:
                current_surf = n
            else:
                right[i] = current_surf-n
        current_surf = 0
        for i  in reversed(range(len(height))):
            if height[i] > current_surf:
                current_surf = height[i]
            else:
                left[i] = current_surf-height[i]
        res= 0
        for i in range(len(height)):
            res+=min(left[i],right[i])
        return res


