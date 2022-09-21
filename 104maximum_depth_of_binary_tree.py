# Runtime: 50 ms, faster than 81.97% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 54.72% of Python3 online submissions for Maximum Depth of Binary Tree.
# TODO: learning - when checking the leaf node, how are you going to return the depth number? +-1 level
#  Try to use the return number as the height of the node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1