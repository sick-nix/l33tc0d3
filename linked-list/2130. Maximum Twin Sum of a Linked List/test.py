from typing import List, Optional
from solution import ListNode, Solution


def from_list_to_linked(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    first = l.pop(0)
    head = ListNode(first)
    prev = head

    for item in l:
        nxt = ListNode(item)
        prev.next = nxt
        prev = nxt

    return head


def from_linked_to_list(head: Optional[ListNode]) -> List[int]:
    l = []
    if head is None:
        return l

    node = head

    while node is not None:
        l.append(node.val)
        node = node.next

    print(l)

    return l


o = Solution()
assert o.pairSum(from_list_to_linked([5, 4, 2, 1])) == 6
assert o.pairSum(from_list_to_linked([4, 2, 2, 3])) == 7
assert o.pairSum(from_list_to_linked([1, 100000])) == 100001
