# TODO: learning - two pointers case!
#  They can

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 113 ms, faster than 18.81% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.6 MB, less than 30.84% of Python3 online submissions for Linked List Cycle.
# Space complexity in O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            # because of the if, we can use the next two lines with .next
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# Runtime: 4210 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.6 MB, less than 67.07% of Python3 online submissions for Linked List Cycle.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        archive = []
        while head:
            if head in archive:
                return True
            else:
                archive.append(head)
                head = head.next
        return False
