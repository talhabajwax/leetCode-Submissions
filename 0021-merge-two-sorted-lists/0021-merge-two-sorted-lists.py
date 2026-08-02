# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(list1,list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            if list1.val <= list2.val:
                list1.next=recursion(list1.next,list2)
                head = list1
            elif list2.val <= list1.val:
                list2.next = recursion(list2.next,list1)
                head = list2
            return head
        return recursion(list1,list2)
        