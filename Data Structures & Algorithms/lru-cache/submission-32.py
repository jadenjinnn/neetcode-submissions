class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        temp = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = temp
        temp.next = node
        # print(node.prev, node.val)

    def remove(self, node):
        # print(self.cache, node.prev)
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insert(self.cache[key])
        else:
            if len(self.cache) >= self.cap:
                rmv = self.left.next
                # print(rmv.value)
                # print(self.cache)
                self.remove(rmv)
                del self.cache[rmv.key]
            
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node 

            

