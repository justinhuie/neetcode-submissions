# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initalize counter for popped integers
        # And stack and cur
        n = 0
        stack = []
        cur = root
        # While stack or curr then while curr iterate until cant go left then pop from stack
        # To make cur non null then increment n by 1 and check if n ==k then try right
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        
        