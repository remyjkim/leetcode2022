# Runtime: 308 ms, faster than 36.08% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 53.5 MB, less than 56.66% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# TODO: learning - inorder allows you to bisect the list into left/right -> use recursive
#  To find the root, find the next root thru preorder and pop it
#  Recursive: just input 0:k and k+1: to the next recursive list

def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root