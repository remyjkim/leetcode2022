# TODO: learning - 1) find the middle node((n+1)//2 th node) 2) reverse the order 3) merge
#  What I did wrong: 1) index of the middle node 2) how to take care of unnecessary next's (some need to be reset)
#  this also involves the order in which you conduct the reversal
#  3) when merging, you the repeat number can be based on the shorter, reversed list (no need


# from the discussion
class Solution:
    def reorderList(self, head):
        # step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        # TODO: alternate head1/head2 between list1 and list2 and just check if the next node is available
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

        # or
        # head1 ,head2 = head, prev
        # while head1 and head2:
        #     nxt1 = head1.next
        #     nxt2 = head2.next
        #
        #     head1.next = head2
        #     head1 = nxt1
        #
        #     head2.next = head1
        #     head2 = nxt2


# Does not work -> creates cycle in the end
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # TODO: think about void list
        mid_ptr = end_ptr = ListNode(0, head)
        length = 0

        # move end_ptr to end
        while end_ptr and end_ptr.next:
            end_ptr = end_ptr.next
            length += 1

        print(length)
        # move mid_ptr to the middle
        for i in range((length + 1) // 2 + 1):
            mid_ptr = mid_ptr.next

        print(f"mid_ptr at {mid_ptr.val}")

        next_ptr, prev = mid_ptr, None
        # reverse the arrow from middle onward
        for i in range(length - ((length + 1) // 2)):
            # print(f"mid:{mid_ptr.val} / next_ptr:{next_ptr.val}")
            next_ptr = mid_ptr.next
            mid_ptr.next = prev
            prev = mid_ptr
            mid_ptr = next_ptr
        mid_ptr = prev
        print(f"head at {head.val} / mid_ptr at {mid_ptr.val}")
        print(f"last ptr's next is : {mid_ptr.next}")
        cur = res = ListNode(0, head)
        for i in range(length):
            if i % 2 == 0:
                cur.next = head
                head = head.next
            else:
                cur.next = mid_ptr
                mid_ptr = mid_ptr.next
            cur = cur.next
            print(f"{i}th: added {cur.val}")
        return res.next