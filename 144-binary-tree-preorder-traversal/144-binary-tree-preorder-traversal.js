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
let ans = []
var preorderTraversalUtil = function(root) {
    if (root) {
        ans.push(root.val)
        preorderTraversalUtil(root.left)
        preorderTraversalUtil(root.right)
    }
}
var preorderTraversal = function(root) {
    ans.length = 0
    preorderTraversalUtil(root)
    return ans
}