# Runtime: 38 ms, faster than 86.27% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.9 MB, less than 70.23% of Python3 online submissions for Remove Nth Node From End of List.
# TODO: learning - only one traversal can do if two pointers advance with n distance apart

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = ListNode(0, head)
        for _ in range(n): fast = fast.next
        if fast.next is None: return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head