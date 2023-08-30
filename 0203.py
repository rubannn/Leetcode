# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        top = ListNode(None)
        top.next = head
        head = top
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next if head.next.next else None
            head = head.next
        return top.next
