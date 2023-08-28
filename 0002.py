# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = 0
        res = ListNode(t)
        v = res
        while l1 or l2:
            t = (l1.val if l1 else 0) + (l2.val if l2 else 0) + t
            v.val = t % 10
            t = t // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2:
                v.next = ListNode()
                v = v.next
            elif t > 0:
                v.next = ListNode(t)
        return res
