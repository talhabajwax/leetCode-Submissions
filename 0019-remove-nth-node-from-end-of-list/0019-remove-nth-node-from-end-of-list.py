# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count =1
        while current.next is not None:
            current =current.next
            count+=1
        current = head
        count2=1
        rem=count - n
        while current.next is not None:
            if count2 == rem:
                current.next = current.next.next
                break
            else:
                current=current.next
                count2+=1
        if rem == 0:
            head = head.next
        return head