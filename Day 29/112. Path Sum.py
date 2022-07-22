# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solver(r,v):
            if not r:
                return False
            v+=r.val
            if not r.left and not r.right:
                return v==targetSum
            if solver(r.left,v):
                return True
            elif solver(r.right,v):
                return True
            return False
        return solver(root,0)