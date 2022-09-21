# Runtime: 86 ms, faster than 30.18% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.4 MB, less than 42.77% of Python3 online submissions for Diameter of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0, 0
            left, right = maxDepth(root.left), maxDepth(root.right)
            max_diam = max(left[0]+right[0], left[1], right[1])
            return [max(left[0], right[0])+1, max_diam]
        return maxDepth(root)[1]