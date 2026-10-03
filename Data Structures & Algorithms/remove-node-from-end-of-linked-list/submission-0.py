# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Offset right and left by n
        while n > 0 and right:
            right = right.next
            n -= 1 
        
        # Increment left and right until right is NULL
        while right:
            left = left.next
            right = right.next
        
        # Delete node at left
        left.next = left.next.next


        # return dummy.next
        return dummy.next
            
        