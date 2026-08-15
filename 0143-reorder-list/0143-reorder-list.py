# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        front = head
        def recursion(back):
            nonlocal front
            if back is None:
                return
            recursion(back.next)
            if front is None:
                return          
            if front is back:
                back.next = None
                front = None
                return
            if front.next is back:
                back.next = None
                front = None
                return
            second = front.next
            front.next = back
            back.next = second
            front = second
        recursion(head)   
        