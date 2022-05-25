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
var postorderTraversalUtil = function(root) {
    if (root) {
        postorderTraversalUtil(root.left)
        postorderTraversalUtil(root.right)
        ans.push(root.val)
    }
}
var postorderTraversal = function(root) {
    ans.length = 0
    postorderTraversalUtil(root)
    return ans
}