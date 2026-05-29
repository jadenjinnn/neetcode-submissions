# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, head1, head2):
        dummy = node = ListNode()

        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
                node = node.next
            else:
                node.next = head2
                head2 = head2.next
                node=node.next

        node.next = head1 or head2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)>1:
            lists.append(self.merge2Lists(lists.pop(), lists.pop()))

        return lists[0] if lists else None
