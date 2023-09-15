# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = 0, 0
        while l1 or l2:
            if l1:
                x = 10 * x + l1.val
                l1 = l1.next
            if l2:
                y = 10 * y + l2.val
                l2 = l2.next
        t = x + y
        res = ListNode()
        while t > 0:
            res.val = t % 10
            t //= 10
            if t:
                node = ListNode()
                node.next = res
                res = node
        return res
