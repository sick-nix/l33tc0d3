from typing import Optional, List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_sum_from_node(node: Optional[TreeNode], s: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val == s:
                count += 1

            count += path_sum_from_node(node.left, s - node.val)
            count += path_sum_from_node(node.right, s - node.val)
            return count

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            count = path_sum_from_node(node, targetSum)

            count += dfs(node.left)
            count += dfs(node.right)

            return count
        return dfs(root)
