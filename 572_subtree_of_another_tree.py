# TODO: learning - KMP algorithms!! serialize and compare" -> O(M+N)
#  learn to ust "return root 1 == root2"

# KMP with LPS algorithm (from discussions - seems best)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            if root == None:
                return ",#"

            return "," + str(root.val) + serialize(root.left) + serialize(root.right)

        def getLPS(s):
            m, j = len(s), 0
            lps = [0] * m
            for i in range(1, m):
                while s[i] != s[j] and j > 0: j = lps[j - 1]
                # TODO: What does this mean? -> we go back to the lps[j-1]th ptr for j and start comparing again
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps

        def kmp(s, p):
            lps = getLPS(p)
            n, m, j = len(s), len(p), 0
            for i in range(n):
                while s[i] != p[j] and j > 0: j = lps[j - 1]
                if s[i] == p[j]:
                    j += 1
                    if j == m: return True
            return False

        return kmp(serialize(root), serialize(subRoot))




# Runtime: 320 ms, faster than 6.68% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.3 MB, less than 12.53% of Python3 online submissions for Subtree of Another Tree.

# My custom KMP algorithm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        print(self.serialize(root), self.serialize(subroot))
        return self.lps(self.serialize(root), self.serialize(subroot))

    def serialize(self, root):
        if root is None:
            return ",#"
        return "," + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def lps(self, haystack, needle):
        if needle == "##": return False
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        # def kmp(self, haystack, needle):
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return True  # i - len(needle)
        return False

# typical alg
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1, root2):
            if root1 == None or root2 == None: return root1 == root2
            return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)

        def dfs(root, subRoot):
            if root == None: return False
            return isEqual(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

# merkle tree
def isSubtree(self, s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()

    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle

    merkle(s)
    merkle(t)

    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or
                dfs(node.left) or dfs(node.right))

    return dfs(s)