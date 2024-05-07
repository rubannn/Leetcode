# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = ListNode(-1, head)
        digit = []
        digit.append(head.val)
        head = head.next
        list_len = 1
        while head:
            digit.append(head.val)
            list_len += 1
            head = head.next

        rest = 0
        for i in range(len(digit) - 1, -1, -1):
            rest, m = divmod(digit[i] * 2 + rest, 10)
            digit[i] = m
        if rest:
            digit = [rest] + digit

        head, i = top, 0
        if len(digit) == list_len:
            head = head.next
        while head:
            head.val = digit[i]
            i += 1
            head = head.next
        return top.next if len(digit) == list_len else top
