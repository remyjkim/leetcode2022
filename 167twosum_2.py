#TODO : why is the left at the end need not be updated? -> related to two pointer mechanism
#Looked at the solution
# Runtime: 174 ms, faster than 69.64% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.9 MB, less than 89.17% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while(left<right):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left +=1
            elif sum > target:
                right -=1
                # left = 0 #