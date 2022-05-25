# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    summ = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left:
                if root.left.left == None and root.left.right == None:
                    self.summ += root.left.val
        if root.left:
            self.sumOfLeftLeaves(root.left)
        if root.right:
            self.sumOfLeftLeaves(root.right)
        return self.summ