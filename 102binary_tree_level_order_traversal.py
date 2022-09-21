# Runtime: 75 ms, faster than 11.77% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 51.51% of Python3 online submissions for Binary Tree Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TODO: learning - much more concise - learn to use double for loop!
#  add to "level" and add children of all the nodes in level to the next level (LRpair as just a stepping stone)
def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        stack = [[root, 0]]
        lev = 0
        res = defaultdict(list)
        if not root:
            return []
        else:
            res[lev].append(root.val)
        while stack:
            if stack[0][1] != lev:
                lev += 1
            if stack[0][0].left:
                stack.append([stack[0][0].left, lev + 1])
                res[lev + 1].append(stack[0][0].left.val)
            if stack[0][0].right:
                stack.append([stack[0][0].right, lev + 1])
                res[lev + 1].append(stack[0][0].right.val)
            stack.pop(0)
        return list(res.values())
