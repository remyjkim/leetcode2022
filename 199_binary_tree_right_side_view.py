# TODO: learning - 1) recursive right side view that only takes the left child's right side view only when it's longer \
#   but the list concatenation at the end is O(n) -> O(n^2) at worst
#   More elaboration: if the tree is unbalanced so that the height is near n/2, the returned list length \
#   would be n/2 in avg
#   2) recursive right side view that first sees the right view, and if it sees something deeper in the left, \
#   adds them to "view"
#   3) get list for each level, only take the right ones
#  Look Carefully into what each dfs function returns!!

# My version
# Runtime: 54 ms, faster than 48.49% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.9 MB, less than 23.63% of Python3 online submissions for Binary Tree Right Side View.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans, level = [], [root]
        while root and level:
            ans.append(level[-1].val)
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans

# 1) O(n^2) at worst, recursive rightside view goes to both the right and the left nodes whatsoever
def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]


# 2) O(n) recursive right side view that only goes deeper if it is in the new depth
def rightSideView(self, root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth + 1)
            collect(node.left, depth + 1)
    view = []
    collect(root, 0)
    return view
