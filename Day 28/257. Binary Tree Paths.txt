# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def solver(r,v):
            if not r:
                ans.append(v[:-2])
                return
            if not r.left:
                solver(r.right,v+str(r.val)+'->')
            elif not r.right:
                solver(r.left,v+str(r.val)+'->')
            else:
                solver(r.left,v+str(r.val)+'->')
                solver(r.right,v+str(r.val)+'->')
        solver(root,"")
        return ans