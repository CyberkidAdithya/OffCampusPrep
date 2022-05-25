/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> ans;
    void preorderTraversalUtil(TreeNode* root) {
        if (root) {
            ans.push_back(root->val);
            preorderTraversalUtil(root->left);
            preorderTraversalUtil(root->right);
        }
    }
    vector<int> preorderTraversal(TreeNode* root) {
        preorderTraversalUtil(root);
        return ans;
    }
};