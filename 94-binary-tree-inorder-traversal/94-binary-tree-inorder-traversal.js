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
    public void inorderTraversalUtil(TreeNode root) {
        if (root != null) {
            this.inorderTraversalUtil(root.left);
            ans.add(root.val);
            this.inorderTraversalUtil(root.right);
        }
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        this.inorderTraversalUtil(root);
        return ans;
    }
}