from typing import Optional, List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)

    def getLeaves(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []
        if root:
            if root.left:
                leaves += self.getLeaves(root.left)
            if root.right:
                leaves += self.getLeaves(root.right)
            if not root.left and not root.right:
                leaves += [root.val]
        return leaves
