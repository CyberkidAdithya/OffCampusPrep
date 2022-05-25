"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if root:
            que = [root,]
            while que:
                sz = len(que)
                print(len(que))
                sub = []
                for i in range(sz):
                    ele = que.pop(0)
                    sub.append(ele.val)
                    for y in ele.children:
                        if y:
                            que.append(y)
                ans.append(sub)
        return ans