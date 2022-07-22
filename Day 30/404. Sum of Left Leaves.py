# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solver(r,s,parity):
            if not r:
                return 0
            if not r.left and not r.right and parity==1:
                s+=r.val
                return s
            return(solver(r.left,s,1)+solver(r.right,s,0))
        return solver(root,0,0)