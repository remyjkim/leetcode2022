# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 38 ms, faster than 81.26% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.8 MB, less than 57.11% of Python3 online submissions for Invert Binary Tree.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
            return root
