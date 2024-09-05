from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head = head
        even_head = head.next

        if not even_head:
            return head

        odd_current = odd_head
        odd_last = odd_head
        even_current = even_head
        even_last = even_head

        current_node = even_head.next
        i = 3

        while current_node != None:
            if i % 2 == 0:
                even_current.next = current_node
                even_current = current_node
                even_last = current_node
            else:
                odd_current.next = current_node
                odd_current = current_node
                odd_last = current_node
            current_node = current_node.next
            i += 1

        odd_last.next = even_head
        even_last.next = None

        return head
