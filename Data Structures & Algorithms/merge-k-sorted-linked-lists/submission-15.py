# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists)>1:
            head1, head2 = lists.pop(), lists.pop()
            dummy = node = ListNode()
            while head1 and head2:
                if head1.val < head2.val:
                    node.next = head1
                    head1 = head1.next
                    node=node.next
                else:
                    node.next = head2
                    head2 = head2.next

                    node=node.next

            node.next = head1 or head2

            lists.append(dummy.next)

        return lists[0]