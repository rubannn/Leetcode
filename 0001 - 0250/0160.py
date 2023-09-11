class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        valA = []
        while headA:
            valA.append(headA)
            headA = headA.next
        while headB:
            if headB in valA:
                return headB
            headB = headB.next
        return
