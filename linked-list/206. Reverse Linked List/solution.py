from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None:
            return head

        new_head = None
        prev = head
        node = head.next

        head.next = None

        while True:
            nxt = node.next
            if nxt is None:
                node.next = prev
                new_head = node
                break
            else:
                node.next = prev
                prev = node
                node = nxt

        return new_head
