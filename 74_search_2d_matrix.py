# Runtime: 89 ms, faster than 15.76% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 43.34% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rownum = len(matrix)
        colnum = len(matrix[0])
        left, right = 0, rownum*colnum-1
        while (left <right):
            mid = (left+right)//2
            if matrix[mid//colnum][mid%colnum] < target:
                left = mid+1
            elif matrix[mid//colnum][mid%colnum] > target:
                right = mid-1
            else:
                return True
        if matrix[left//colnum][left%colnum]==target:
            return True
        return False
