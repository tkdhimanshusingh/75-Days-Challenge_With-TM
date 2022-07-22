# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        flag=0
        q=collections.deque()
        q.append(root)
        while q:
            level=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if flag:
                    ans.append(level[::-1])
                    flag=0
                else:
                    ans.append(level)
                    flag=1
        return ans