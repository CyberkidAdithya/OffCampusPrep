# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root: queue.append(root)
        levels = []
        while queue:
            sz = len(queue)
            level = []
            for i in range(sz):
                x = queue.pop(0)
                level.append(x.val)
                if x.left: queue.append(x.left)
                if x.right: queue.append(x.right)
            levels.append(level)
        return levels[::-1] if root else []