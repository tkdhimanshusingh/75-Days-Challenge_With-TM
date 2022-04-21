# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def solver(r1,r2):
            if r1 and r2:
                ans=TreeNode(r1.val+r2.val)
                ans.left=solver(r1.left,r2.left)
                ans.right=solver(r1.right,r2.right)
                #return ans
            elif r1:
                ans=TreeNode(r1.val)
                ans.left=solver(r1.left,0)
                ans.right=solver(r1.right,0)
            elif r2:
                ans=TreeNode(r2.val)
                ans.left=solver(0,r2.left)
                ans.right=solver(0,r2.right)
            else:
                return
            return ans
        return solver(root1,root2)
                