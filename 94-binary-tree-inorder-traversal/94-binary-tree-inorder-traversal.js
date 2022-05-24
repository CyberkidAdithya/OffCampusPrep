/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const ans = []
var inorderTraversalUtil = function(root) {
    if (root) {
        inorderTraversalUtil(root.left)
        ans.push(root.val)
        inorderTraversalUtil(root.right)
    }
}
var inorderTraversal = function(root) {
    ans.length = 0
    inorderTraversalUtil(root)
    return ans
};