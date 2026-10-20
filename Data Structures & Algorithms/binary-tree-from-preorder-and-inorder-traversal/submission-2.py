# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid +1, right)
            return root

        return dfs(0, len(inorder) - 1)
        # preorder is node, left, right
        # inorder is left. node, right

        # if we have tree [1 2 3 4 5 6 7]
        # our preorder would be
        # [1 2 3 4 5 6 7]
        # our inorder would be
        # [4 2 5 1 6 3 7]

