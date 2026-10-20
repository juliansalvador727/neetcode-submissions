# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # clearly this is a recursive solution
        # let node be the current node, left be the left child of node and right be the right child of node
        # for every node we check that left is less than node. and we check right is greater than node
        # then, we push left and right into our queue
        # repeat using bfs
        # if our condition does not hold true for any node, then return false.
        # else if we have traversed through the tree correctly, return true
        q = collections.deque([(root, float("-inf"), float("inf"))])

        while q:
            node, lb, ub = q.popleft()
            if not (lb < node.val < ub):
                return False
            if node.left:
                q.append((node.left, lb, node.val))
            if node.right:
                q.append((node.right, node.val, ub))
        
        return True

