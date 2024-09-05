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
assert o.pathSum(from_list_to_tree(
    [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3
assert o.pathSum(from_list_to_tree(
    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == 3
