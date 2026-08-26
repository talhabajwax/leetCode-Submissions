# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self,head:Optional[ListNode],x:int)->Optional[ListNode]:
        current=head
        smallHead=None
        smallTail=None
        bigHead=None
        bigTail=None
        while current is not None:
            nextNode=current.next
            current.next=None
            if current.val<x:
                if smallHead is None:
                    smallHead=current
                    smallTail=current
                else:
                    smallTail.next=current
                    smallTail=current
            else:
                if bigHead is None:
                    bigHead=current
                    bigTail=current
                else:
                    bigTail.next=current
                    bigTail=current
            current=nextNode
        if smallHead is None:
            return bigHead
        smallTail.next=bigHead
        return smallHead