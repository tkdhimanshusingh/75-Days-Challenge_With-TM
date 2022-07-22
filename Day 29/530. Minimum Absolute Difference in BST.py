# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global ans,prev
        prev=None
        ans=float('inf')
        def solver(r):
            global ans,prev
            if not r:
                return
            solver(r.left)
            if prev!=None:
                ans=min(ans,r.val-prev)
            prev=r.val
            solver(r.right)
        solver(root)
        return(ans)