class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to nodes
        # Left is for LRU
        # Right is for MRU
        self.left = Node(0,0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove from list   
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Insert at right
    def insert(self, node):
        prev = self.right.prev
        self.right.prev = node
        prev.next = node
        node.next = self.right
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # Node already exist with same key val
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Remove LRU from linked list and cache (left.next)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
