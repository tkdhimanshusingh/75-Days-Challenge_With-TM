# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solver(r):
            if not r:
                return
            elif p.val==r.val or q.val==r.val:
                return r
            elif p.val>r.val and q.val>r.val:
                ans=solver(r.right)
            elif p.val<r.val and q.val<r.val:
                ans=solver(r.left)
            elif (q.val>r.val and p.val<r.val) or (q.val<r.val and p.val>r.val):
                return r
            return ans
        return solver(root)