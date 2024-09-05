from typing import List, Optional
from solution import TreeNode, Solution


def from_list_to_tree(l: List[Optional[int]]) -> Optional[TreeNode]:
    """Create BT from list of values."""
    n = len(l)

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


def to_tree_node(root: Optional[TreeNode]) -> TreeNode:
    if root:
        return root
    return TreeNode()


o = Solution()
assert o.goodNodes(to_tree_node(
    from_list_to_tree([3, 1, 4, 3, None, 1, 5]))) == 4
assert o.goodNodes(to_tree_node(from_list_to_tree([3, 3, None, 4, 2]))) == 3
assert o.goodNodes(to_tree_node(from_list_to_tree([1]))) == 1
assert o.goodNodes(to_tree_node(from_list_to_tree([9, None, 3, 6]))) == 1
