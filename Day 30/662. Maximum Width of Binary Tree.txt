# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=queue.deque()
        q.append([root,0])
        mx=0
        while(q):
            count=len(q)
            l=q[0][1]
            for i in range(count):
                node=q.popleft()
                m=node[1]
                if node[0].left:
                    q.append([node[0].left,2*node[1]+1])
                if node[0].right:
                    q.append([node[0].right,2*node[1]+2])
            mx=max(mx,m-l+1)
        return(mx)