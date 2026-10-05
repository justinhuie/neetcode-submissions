# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case #1
        if not p and not q:
            return True
        # If only one is null then false
        if not p or not q or p.val != q.val:
            return False
        
        # p and q are non empty and same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            

       

        

        