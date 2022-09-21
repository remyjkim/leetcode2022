# Runtime: 77 ms, faster than 43.10% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.6 MB, less than 46.88% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, range_=[float("-inf"), float("inf")]):
            if not root:
                return True
            if not(range_[0]< root.val < range_[1]):
                return False
            return dfs(root.left, (range_[0], root.val)) and dfs(root.right, (root.val, range_[1]))
        return dfs(root)