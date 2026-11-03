# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            a = list1.val
            b = list2.val
            if (a < b):
                tail.next = list1
                list1 = list1.next
            elif (a >= b):
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 else list2
        
        return dummy.next
                
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None


        # start at gap=1, multiply gap by 2 until gap < lists.size()
        # start at i = 0, do i += gap *2 until i + gap < lists.size()

        gap = 1
        while gap < len(lists):
            i = 0
            while i + gap < len(lists):
                lists[i] = self.merge(lists[i], lists[i+gap])
                i = i + gap*2
            gap = gap * 2
        return lists[0]