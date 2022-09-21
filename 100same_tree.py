# Runtime: 33 ms, faster than 91.24% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 29.20% of Python3 online submissions for Same Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p and q):
            return p==q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)