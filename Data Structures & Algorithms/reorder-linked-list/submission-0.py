# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast and slow pointers to find half way point of list
        # Reverse second part of list
        # Merge two lists

        fast = head
        slow = head
        # Slow.next now head of second list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        # Reverse second part of list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Now prev is at head of reversed list
        second = prev
        first = head
        # Merge two lists
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        