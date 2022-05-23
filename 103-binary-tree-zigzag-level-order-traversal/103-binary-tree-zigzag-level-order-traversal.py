# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root:
            queue = [root]
            direction = 1
            while queue:
                sz = len(queue)
                sub = []
                for i in range(sz):
                    ele = queue.pop(0)
                    sub.append(ele.val)
                    if ele.left:
                        queue.append(ele.left)
                    if ele.right:
                        queue.append(ele.right)
                levels.append(sub[::direction])
                direction *= -1
        return levels