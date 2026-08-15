# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(head):
            if head is None:
                return head
            if head.next is None :
                return head
            second = head.next
            rest = second.next
            second.next = head
            head.next=recursion(rest)
            return second
        return recursion(head)

        