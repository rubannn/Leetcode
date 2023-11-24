# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        k = 0
        while node:
            k += 1
            node = node.next
        k = k // 2
        if k == 0:
            return None

        node = head
        while k > 1:
            k -= 1
            node = node.next
        node.next = node.next.next
        return head
