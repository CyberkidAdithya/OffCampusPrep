class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        temp = node.next.next
        node.next = temp