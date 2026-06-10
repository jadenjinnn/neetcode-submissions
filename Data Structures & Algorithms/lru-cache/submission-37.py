class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def insert(self, node):
        temp = self.right.prev
        self.right.prev = node
        temp.next = node
        node.prev = temp
        node.next = self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)

            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
                
        
        
