# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elems = []
        for v in lists:
            while v:
                elems.append(v.val)
                v = v.next
        elems.sort()
        top = head = ListNode(None)
        for elem in elems:
            cur = ListNode(elem)
            head.next = cur
            head = cur
        return top.next
