# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0
        def dfs(root, biggest):
            nonlocal sol
            if not root:
                return None

            if root.val >= biggest:
                sol += 1
            
            dfs(root.left, max(biggest, root.val))
            dfs(root.right, max(biggest, root.val))

        dfs(root, float("-inf"))
        return sol