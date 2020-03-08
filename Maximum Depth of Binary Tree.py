#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        result = []
        #create a queue
        queue = deque()
        #append the root value in the queue
        queue.append(root)
        #create a varibale depth to maintain the level of depth in the trr
        depth = 0
        # it iterates until the queue is empty, here we incerement depth and maintain the size of the queue because we add values of right and left children in the tree
        while queue:
            depth += 1
            size = len(queue)
            print(depth)
            temp = []
            for _ in range(size):
                
                currrent = queue.popleft()
                temp.append(currrent.val)
                if currrent.left:
                    queue.append(currrent.left)
                if currrent.right:
                    queue.append(currrent.right)
        return depth



