# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        cur = slow.next
        prev = slow.next = None
# 1 > 2 > 3 > 4 > 5
#         ^             ^
        while cur:
            temp = cur.next

            cur.next = prev
            prev = cur
            cur = temp
        
        sol = head

        while prev:
            t1, t2 = head.next, prev.next
            head.next = prev
            head.next.next = t1
            head = head.next.next
            prev = t2

        head = sol