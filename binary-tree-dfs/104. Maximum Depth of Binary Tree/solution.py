from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.getMaxDepth(root)
        return depth

    def getMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.getMaxDepth(root.left), self.getMaxDepth(root.right)) + 1
