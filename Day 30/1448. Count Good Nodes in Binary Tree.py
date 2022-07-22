# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global cnt
        cnt=0
        def solver(root,mx):
            global cnt
            if not root:
                return cnt
            if mx<=root.val:
                cnt+=1
            mx=max(mx,root.val)
            if root.left:
                solver(root.left,mx)
            if root.right:
                solver(root.right,mx)
        solver(root,root.val)
        return cnt