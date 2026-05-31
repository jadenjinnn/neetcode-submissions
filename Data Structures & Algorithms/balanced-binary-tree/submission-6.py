# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        sol = True
        
        def dfs(root):
            nonlocal sol

            if not root:
                return 0

            d1 = dfs(root.left)
            d2 = dfs(root.right)

            if abs(d1-d2) > 1:
                sol = False

            return 1+max(dfs(root.left), dfs(root.right))

        dfs(root)

        return sol