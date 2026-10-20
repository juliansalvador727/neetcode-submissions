# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is trivially good
        # at the start, keep track of the value of root, call this k
        # run bfs / dfs on the tree
        # when we see node.val >= k, that node is good.
        # keep a counter for every node.val > k we see. return counter

        if not root:
            return 0
        count = 0
        q = collections.deque([(root, root.val)])

        while q:
            node, k = q.popleft()

            if node.val >= k:
                count += 1
            
            k = max(k, node.val)

            if node.left:
                q.append((node.left, k))
            if node.right:
                q.append((node.right, k))
        
        return count