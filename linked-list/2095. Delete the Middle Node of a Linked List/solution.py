from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next

        if length == 1:
            return None

        idx_to_delete = length // 2

        prev = head
        node = head.next
        i = 0
        while i < idx_to_delete - 1:
            prev = node
            if node:
                node = node.next
            i += 1

        if prev and node:
            prev.next = node.next

        return head
