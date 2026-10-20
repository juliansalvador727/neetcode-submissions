# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use recursive dfs, start from leaves
        if root is None:
            return None

        st = [root]
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)

        return root