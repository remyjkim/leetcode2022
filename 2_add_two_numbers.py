# Runtime: 118 ms, faster than 41.60% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 9.84% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = tmp = ListNode(0)
        carry = 0
        while l1 or l2:
            # print(l1, '/', l2)
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            tmp.next = ListNode((l1val+ l2val +carry) % 10)
            carry = (l1val+ l2val +carry) // 10
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            tmp = tmp.next
        if carry:
            tmp.next = ListNode(1)
        return res.next