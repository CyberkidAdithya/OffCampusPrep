# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    que = []
    def __init__(self):
        self.que = []
    def enqueue(self, nbr):
        self.que.append(nbr)
    def dequeue(self):
        return self.que.pop(0)
    def __len__(self):
        return len(self.que)
    
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        que = []
        anss = 0
        if root:
            levels = []
            que.append(root)
            while que:
                sz = len(que)
                sub = []
                for i in range(sz):
                    x = que.pop(0)
                    sub.append(x.val)
                    if x.left:
                        que.append(x.left)
                    if x.right:
                        que.append(x.right)
                levels.append(sub)
                anss = sum(sub)
        return anss