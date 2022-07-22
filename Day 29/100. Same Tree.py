# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solver(r1,r2):
            if not r1 and not r2:
                return True
            elif (r1 and not r2) or (not r1 and r2) or (r1.val!=r2.val):
                return False
            if solver(r1.left,r2.left)==False:
                return False
            if solver(r1.right,r2.right)==False:
                return False
            return True
        return(solver(p,q))