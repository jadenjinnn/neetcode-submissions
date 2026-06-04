# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = dummy = ListNode(next=head)

        groupPrev = dummy
        i = 1

        while True:
            node = groupPrev
            for _ in range(k):
                node = node.next
                
                if not node:
                    return dummy.next

            

            groupNext = node.next

            prev, cur = node.next, groupPrev.next

            while cur != groupNext:
                temp = cur.next
            
                cur.next = prev
                prev = cur
                cur = temp

            tmp=groupPrev.next
            groupPrev.next = node
            groupPrev = tmp

        

            

            