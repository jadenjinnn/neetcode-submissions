# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        while len(lists)>1:
            dummy = node = ListNode()

            l1 = lists.pop()
            l2 = lists.pop()

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next

                node = node.next

            node.next = l1 or l2

            lists.append(dummy.next)

        return lists[0]