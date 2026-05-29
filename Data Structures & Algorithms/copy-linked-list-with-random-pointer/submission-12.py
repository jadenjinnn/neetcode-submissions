"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = defaultdict(lambda: Node(0))
        oldtonew[None] = None
        n = head

        while head:
            oldtonew[head].val = head.val
            oldtonew[head].next = oldtonew[head.next]
            oldtonew[head].random = oldtonew[head.random]

            head = head.next

        return oldtonew[n]