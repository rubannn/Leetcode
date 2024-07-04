# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = res = ListNode()
        k = 0
        head = head.next
        while head:
            if head.val != 0:
                k += head.val
            else:
                res.next = ListNode(k)
                res = res.next
                k = 0
            head = head.next
        return top.next
