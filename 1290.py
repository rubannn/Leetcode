class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = ''
        while head:
            b += str(head.val)
            head = head.next
        return int(b, 2)
