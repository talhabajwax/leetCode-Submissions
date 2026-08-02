# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def recursion(head):
            if head is None:
               return head
            if head.val == val:
                head = recursion(head.next)
                return head
            if head.val != val:
                head.next = recursion(head.next)
                return head
        return recursion(head)
        