# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if not nodes:
            return None
        k %= len(nodes)
        nodes[-1].next = nodes[0]
        nodes[-k-1].next = None
        return nodes[-k]
