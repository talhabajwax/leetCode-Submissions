# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(head):
            if head is None:
                return head
            if head.next is None:
                return head
            node1 = recursion(head.next)
            head.next.next = head
            head.next= None
            return node1
        return recursion(head)