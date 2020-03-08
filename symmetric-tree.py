# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        q = collections.deque()
        q.append((root.left, root.right))
        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2: continue
            if  (not node1 or not node2) or node1.val != node2.val:
                return False
            q.append((node1.left,node2.right))
            q.append((node1.right, node2.left))
        return True
                
           
                    
                    
        
