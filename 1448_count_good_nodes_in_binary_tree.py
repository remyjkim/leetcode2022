# Runtime: 358 ms, faster than 70.07% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 32.7 MB, less than 19.03% of Python3 online submissions for Count Good Nodes in Binary Tree.
# TODO: learning - learn to use good return values - but this may be costly at worst cases for some probs
#  just add True to the return list - we're only counting the number, not returning the whole list!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_num):
            if not root:
                return
            elif root.val >= max_num:
                view.append(root.val)
                max_num = max(root.val, max_num)
            dfs(root.left, max_num)
            dfs(root.right, max_num)
            return
        view = []
        dfs(root, -float("inf"))
        return len(view)


# one-liner
    def goodNodes(self, r, ma=-10000):
        return self.goodNodes(r.left, max(ma, r.val)) + self.goodNodes(r.right, max(ma, r.val)) + (r.val >= ma) if r else 0