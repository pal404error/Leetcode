# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def coun(root):
            if not root:
                return 0
            
            leftcoins = coun(root.left)
            rightcoins = coun(root.right)
            
            self.ans += abs(leftcoins) + abs(rightcoins)
            
            return root.val + leftcoins + rightcoins-1
        
        coun(root)
        return self.ans