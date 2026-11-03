# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode], k: int):
        cur = head
        prev = None

        for _ in range(k):
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        
        return prev, cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count = count + 1
        n = count // k
        
        dummy = ListNode(head, 0)
        prev_tail = dummy
        for _ in range(n):
            group_tail = head

            new_head, next_group = self.reverse_list(head, k)

            prev_tail.next = new_head

            group_tail.next = next_group

            prev_tail = group_tail
            head = next_group
        return dummy.next