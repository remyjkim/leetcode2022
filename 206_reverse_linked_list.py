# Runtime: 34 ms, faster than 96.91% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.5 MB, less than 55.64% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head and head.next:
            next_head = head.next
            head.next = prev
            prev = head
            head = next_head
        if head:
            head.next = prev
        return head