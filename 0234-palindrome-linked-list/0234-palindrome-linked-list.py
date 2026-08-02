# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def recursion(head):
            if head is None:
                return False
            if head.next is  None:
                return True
            current = head
            value=[]
            value.append(current.val)
            reverse=[]
            while current.next is not None:
                current = current.next
                value.append(current.val)
                
            reverse =value[::-1]
            if value == reverse:
                return True
            else:
                return False
        return recursion(head)
                