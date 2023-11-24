# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top_odd = odd_node = ListNode(None)
        top_even = even_node = ListNode(None)
        while head:
            odd_node.next = head
            odd_node = odd_node.next

            even_node.next = head.next
            even_node = even_node.next

            head = head.next.next if head.next else None

        odd_node.next = top_even.next
        return top_odd.next
