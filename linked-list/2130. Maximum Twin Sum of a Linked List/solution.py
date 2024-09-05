from typing import Optional, List


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        l: List[int] = []
        while node != None:
            l.append(node.val)
            node = node.next

        if len(l) == 2:
            return l[0] + l[1]

        s = 0
        mid = len(l) // 2
        while mid > 0:
            s = max(s, l[mid - 1] + l[-mid])
            mid -= 1

        return s
