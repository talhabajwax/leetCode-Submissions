# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        flow=set()
        while headA is not None:
            flow.add(headA)
            headA=headA.next
        while headB is not None:
            if headB  in flow:
                return headB
            if headB not in flow:
                headB=headB.next
                

        