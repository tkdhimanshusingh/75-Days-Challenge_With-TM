# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.solver(root.left,root.right):
            return True
        return False
    def solver(self,l,r):
        if not l and not r:
            return True
        if (not l and r) or (l and not r):
            return False
        if l.val==r.val:
            return (self.solver(l.left,r.right) and self.solver(l.right,r.left))
        return False