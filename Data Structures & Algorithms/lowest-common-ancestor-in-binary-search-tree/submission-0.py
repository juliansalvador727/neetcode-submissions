# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this would be really easy if for every node we store a pointer to its parent and the level
        # just traverse the lower of {p, q} towards the root until we reach a common parent

        # unfortunately we cant do that so we must start at root.
        # at root, dfs downwards until we find p (whichever one we find first lets call p)
        # at p, we conduct another dfs looking for q.
        # if q is not here, then q is either an ancestor of p (which is impossible since we just traversed downards), therefore any of p's parent could be the lowest common ancestor.

        if root is None or root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        
        return left if not right else right