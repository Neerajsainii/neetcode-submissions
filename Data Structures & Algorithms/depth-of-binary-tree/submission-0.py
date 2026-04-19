# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # stack = []
        # h = 0
        # stack.append(root)
        # while stack:
        #     cur = stack.pop()
        #     h += 1
        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)
        if root is None:
            return 0
        h = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        return h 
        
        