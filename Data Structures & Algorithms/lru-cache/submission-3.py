class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node): # Remove node from cache
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert(self, node): # Insert at MRU
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # If key in cache then remove it first then add it
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # If exceeding capacity then remove LRU node from cache
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
