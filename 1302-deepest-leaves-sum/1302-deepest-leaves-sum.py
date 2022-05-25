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
    List<List<Integer>> ans = new ArrayList<>();
    int summ = 0;
    public int deepestLeavesSum(TreeNode root) {
        if (root != null) {
            Queue<TreeNode> que = new LinkedList<>();
            que.add(root);
            while (que.size() > 0) {
                int sz = que.size();
                int presum = 0;
                List<Integer> sub = new ArrayList<>();
                for (int i = 0; i < sz; i++) {
                    TreeNode curr = que.remove();
                    sub.add(curr.val);
                    presum += curr.val;
                    if (curr.left != null) {
                        que.add(curr.left);
                    }
                    if (curr.right != null) {
                        que.add(curr.right);
                    }
                }
                ans.add(sub);
                summ = presum;
            }
        }
        return summ;
    }
}