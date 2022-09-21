# Runtime: 42 ms, faster than 84.88% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.9 MB, less than 83.05% of Python3 online submissions for Copy List with Random Pointer.

# TODO: learning - use hashmaps when you need to match nodes 1-1!
#  Think carefully about which ptrs to start with, and how to initialize them efficiently
#  When using while loop, use 'while ptr' rather than 'while ptr.next'


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp1 = head
        res = tmp2 = Node(0)
        hashmap = {}
        while tmp1:
            tmp2.next = Node(tmp1.val)
            hashmap[tmp1] = tmp2.next
            tmp1, tmp2 = tmp1.next, tmp2.next

        tmp3, tmp4 = head, res.next
        while tmp3:
            if tmp3.random:
                tmp4.random = hashmap[tmp3.random]
            else:
                tmp4.random = None
            tmp3, tmp4 = tmp3.next, tmp4.next
        return res.next
