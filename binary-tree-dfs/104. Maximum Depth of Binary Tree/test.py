from typing import List, Optional
from solution import TreeNode, Solution


def from_list_to_tree(l: List[Optional[int]]) -> Optional[TreeNode]:
    """Create BT from list of values."""
    n = len(l)
    if n == 0:
        return None

    def inner(index: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        if n <= index or l[index] is None:
            return None

        v = l[index]
        node = None
        if v:
            node = TreeNode(v)
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
        return node

    return inner()


o = Solution()
assert o.maxDepth(from_list_to_tree([3, 9, 20, None, None, 15, 7])) == 3
assert o.maxDepth(from_list_to_tree([1, None, 2])) == 2
