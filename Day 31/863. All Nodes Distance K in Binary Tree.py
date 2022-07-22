# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def mark_parents(node, parent = None):
            if node:
                node.parent = parent
                mark_parents(node.left, node)
                mark_parents(node.right, node)
        mark_parents(root)
        
        
        queue = collections.deque()
        visited = set()
        queue.append((target, 0))
        result = []
        
        while queue:
            node, distance = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            if distance == k:
                result.append(node.val)
                continue
            neighbors = [node.parent, node.left, node.right]
            for neighbor in neighbors:
                if neighbor:
                    queue.append((neighbor, distance + 1))

        
        return result