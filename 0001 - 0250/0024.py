from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = node = ListNode()
        while head and head.next:
            tmp = head.next.next
            node.next = head.next
            head.next.next = head
            node = head
            head = tmp
        node.next = head
        return top.next
