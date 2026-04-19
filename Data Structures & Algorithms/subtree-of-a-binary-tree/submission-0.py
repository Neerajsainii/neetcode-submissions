# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or (root and not subRoot):
            return True
        if not root and subRoot:
            return False
        if not self.isSameTree(root,subRoot):
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            return True

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        stack1.append(p)
        stack2.append(q)
        if p.val != q.val:
            return False
        while stack1 or stack2:
            cur1 = stack1.pop() if stack1 else None
            cur2 = stack2.pop() if stack2 else None
            # print('cur1,cur2',cur1,cur2)
            if (cur1.left and not cur2.left) or (not cur1.left and cur2.left):
                return False
            if (cur1.right and not cur2.right) or (not cur1.right and cur2.right):
                return False
            if cur1.left and cur2.left:
                stack1.append(cur1.left)
                stack2.append(cur2.left)
                if cur1.left.val != cur2.left.val:
                    return False
            if cur1.right and cur2.right:
                stack1.append(cur1.right)
                stack2.append(cur2.right)
                if cur1.right.val != cur2.right.val:
                    return False
        return True
        