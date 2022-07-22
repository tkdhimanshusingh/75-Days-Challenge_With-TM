# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ans=[]
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            self.ans.append(r.val)
            dfs(r.right)
        dfs(root)

    def next(self) -> int:
        return self.ans.pop(0)

    def hasNext(self) -> bool:
        if self.ans:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()