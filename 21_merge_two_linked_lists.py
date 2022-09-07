# Runtime: 60 ms, faster than 47.51% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.8 MB, less than 98.86% of Python3 online submissions for Merge Two Sorted Lists.
# TODO: learning - 1) start with a dummy ptr 2) you can just use the given list1, list2 knowing
#  that they are already 'call by reference'

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next