# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        mx = arr[0] + arr[-1]
        for i in range(0, len(arr) // 2):
            tmp = arr[i] + arr[len(arr) - i - 1]
            if tmp > mx:
                mx = tmp
        return mx
