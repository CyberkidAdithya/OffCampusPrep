/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
let ans = []
var preorderUtil = function(root) {
    if (root) {
        ans.push(root.val)
        root.children.forEach((ele) => preorderUtil(ele))
    }
}
var preorder = function(root) {
    ans.length = 0
    preorderUtil(root)
    return ans
};