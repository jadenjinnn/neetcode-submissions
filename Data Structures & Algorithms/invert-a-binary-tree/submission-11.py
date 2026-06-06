# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverse(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.reverse(root.left)
        self.reverse(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root)

        return root