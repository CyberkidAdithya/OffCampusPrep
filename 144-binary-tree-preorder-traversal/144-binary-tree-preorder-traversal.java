/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> ans = new ArrayList<>();
    public void preorderTraversalUtil(TreeNode root) {
        if (root != null) {
            ans.add(root.val);
            this.preorderTraversalUtil(root.left);
            this.preorderTraversalUtil(root.right);
        }
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        this.preorderTraversalUtil(root);
        return ans;
    }
}