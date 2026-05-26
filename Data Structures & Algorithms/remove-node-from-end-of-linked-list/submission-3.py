# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head

        while n:
            r = r.next
            n -= 1

        prev = None

        while r:
            prev = l
            l = l.next
            r = r.next

        if prev is None:
            return l.next

        prev.next = l.next

        return head