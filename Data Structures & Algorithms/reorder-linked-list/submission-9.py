# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        sol = head

        # 2 > 4 > 6 | 8 < 10

        while prev:
            t1 = head.next

            head.next = prev
            prev = prev.next
            head.next.next = t1
            head = t1

        head = sol
