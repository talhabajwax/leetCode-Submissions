class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        while head is not None and head.next is not None and head.val == head.next.val:
            duplicate = head.val

            while head is not None and head.val == duplicate:
                head = head.next

        if head is None:
            return None

        first = head
        current = head.next

        while current is not None:
            current2 = current.next

            if current2 is not None and current.val == current2.val:
                duplicate = current.val

                while current is not None and current.val == duplicate:
                    current = current.next

                first.next = current

            else:
                first = current
                current = current.next

        return head