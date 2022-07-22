class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ans=[]
        pointer=root
        while pointer:
            self.ans.append(pointer)
            pointer=pointer.left

    def next(self) -> int:
        node=self.ans.pop()
        pointer=node.right
        while pointer:
            self.ans.append(pointer)
            pointer=pointer.left
        return node.val
    def hasNext(self) -> bool:
        if self.ans:
            return True
        return False