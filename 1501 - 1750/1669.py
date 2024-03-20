# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        first_list2 = list2
        last_list2 = list2
        while list2:
            last_list2 = list2
            list2 = list2.next

        top = ListNode(0, list1)
        prev = top
        pos = 0
        while list1:
            if pos == a:
                prev.next = first_list2
            if pos == b:
                last_list2.next = list1.next
            prev = list1
            list1 = list1.next
            pos += 1
        return top.next
