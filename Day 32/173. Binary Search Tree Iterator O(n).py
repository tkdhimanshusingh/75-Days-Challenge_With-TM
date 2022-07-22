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
