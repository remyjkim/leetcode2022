# TODO: learning - what is a binary search tree? Use its charateristic to your benefit
#  Also use recursives when you can -> You only need to return the root
#  Do not use inline function dfs()!!!

# Traditional Binary Search Tree
def lowestCommonAncestor(self, root, p, q):
    a, b = sorted([p.val, q.val])
    while not a <= root.val <= b:
        root = (root.left, root.right)[a > root.val]
    return root

# Runtime: 84 ms, faster than 91.49% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.7 MB, less than 96.94% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Using BST's characteristics to its best
def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val] # p,q both on right side
    return root

# recursive
def lowestCommonAncestor(self, root, p, q):
    next = p.val < root.val > q.val and root.left or \
           p.val > root.val < q.val and root.right
    return self.lowestCommonAncestor(next, p, q) if next else root