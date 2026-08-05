class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.right = ListNode(0)
        self.left = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.right:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prev = self.left
        next = self.left.next
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = node
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prev = self.right.prev
        next = self.right
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node = ListNode(val)
            next = cur
            prev = cur.prev
            next.prev = node
            prev.next = node
            node.next = next
            node.prev = prev
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.right:
            next = cur.next
            prev = cur.prev
            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)