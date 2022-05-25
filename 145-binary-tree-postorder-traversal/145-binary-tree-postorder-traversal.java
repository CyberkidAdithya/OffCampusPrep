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
    public void postorderTraversalUtil(TreeNode root) {
        if (root != null) {
            postorderTraversalUtil(root.left);
            postorderTraversalUtil(root.right);
            ans.add(root.val);
        }
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        postorderTraversalUtil(root);
        return ans;
    }
}