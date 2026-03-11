# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0

            leftt = dfs(node.left)
            if leftt == -1:
                return -1
            
            rightt = dfs(node.right)
            if rightt ==-1:
                return -1

            if abs(leftt-rightt)>1:
                return -1
            
            return 1+max(leftt, rightt)
        
        return dfs(root) !=-1