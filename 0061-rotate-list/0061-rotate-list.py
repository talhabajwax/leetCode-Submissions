# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if k==0:
            return head
        slow =head
        fast =head
        count=0
        countHead=head
        length=1
        while countHead.next is not None:
            countHead=countHead.next
            length+=1
        k = k % length
        if k==0:
            return head
        while count<k:
            fast=fast.next
            count+=1
        while fast.next is not None:
            fast=fast.next
            slow=slow.next 
        temp1=slow.next
        slow.next = None
        temp2=head
        head=temp1
        fast.next=temp2
        length=0
        return head




'''        count =0
        while count !=k:
            temp = head
            temp2=None
            while temp.next.next is not None:
                temp = temp.next
            if temp.next.next is None:
                temp2=temp.next
                temp.next=None
                temp3=head
                head=temp2
                temp2.next=temp3
                count+=1
        return head'''
            

        