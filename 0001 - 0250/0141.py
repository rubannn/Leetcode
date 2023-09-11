class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        link = []
        while head:
            x = id(head)
            if x not in link:
                link.append(x)
            else:
                return True
            head = head.next
        return False
