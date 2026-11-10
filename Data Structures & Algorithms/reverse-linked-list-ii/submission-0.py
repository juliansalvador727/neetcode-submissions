# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        before = dummy

        for _ in range(left - 1):
            before = before.next
        
        tail = before.next
        cur = tail
        prev = None

        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        before.next = prev
        tail.next = cur

        return dummy.next
        