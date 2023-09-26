# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        top = res
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    t = ListNode(list1.val)
                    list1 = list1.next
                else:
                    t = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                t = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                t = ListNode(list2.val)
                list2 = list2.next
            res.next = t
            res = res.next
        return top.next
