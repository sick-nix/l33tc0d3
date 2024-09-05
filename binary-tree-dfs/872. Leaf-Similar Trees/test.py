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
assert o.leafSimilar(
    from_list_to_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
    from_list_to_tree([3, 5, 1, 6, 7, 4, 2, None, None,
                      None, None, None, None, 9, 8])
) == True
assert o.leafSimilar(from_list_to_tree(
    [1, 2, 3]), from_list_to_tree([1, 3, 2])) == False
