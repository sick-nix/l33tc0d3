class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recGoodNodes(root, root.val)

    def recGoodNodes(self, root: TreeNode, prev: int) -> int:
        current = root.val

        count = 0
        if prev <= current:
            count += 1
        if root.left:
            count += self.recGoodNodes(root.left, max(current, prev))
        if root.right:
            count += self.recGoodNodes(root.right, max(current, prev))
        return count
