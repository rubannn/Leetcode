# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nodes = head
        if nodes and nodes.next:
            head = nodes.next
        last = ListNode(None)
        while nodes and nodes.next:
            node1 = nodes
            node2 = nodes.next
            print(node1, node2, sep='\n')
            last = node2.next

            node2.next = node1
            node1.next = last
            print('===')
            print(node1, node2, sep='\n')
            nodes = last
        print('~~~\n', head)
        return head
