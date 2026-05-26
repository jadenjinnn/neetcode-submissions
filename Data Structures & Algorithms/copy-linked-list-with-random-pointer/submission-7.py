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
        nodes = {}

        start = head
        newhead = sol = Node(0)

        while head:
            new = Node(head.val)
            sol.next = new
            sol = sol.next
            nodes[head] = new
            head = head.next

        sol = newhead = newhead.next

        while start:
            if start.random:
                newhead.random = nodes[start.random]
            newhead =newhead.next
            start = start.next

        return sol