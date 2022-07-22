class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def dfs(root):
            global ans
            if not root:
                return -1
            left=dfs(root.left)
            right=dfs(root.right)
            ans=max(ans,2+left+right)
            return 1+max(left,right)
        dfs(root)
        return ans