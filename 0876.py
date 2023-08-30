class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head)
            head = head.next
        return vals[len(vals) // 2]
