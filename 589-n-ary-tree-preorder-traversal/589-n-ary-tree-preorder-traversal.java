/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    List<Integer> ans = new ArrayList<Integer>();
    public void preorderUtil(Node root) {
        if (root != null) {
            ans.add(root.val);
            for (Node child: root.children) {
                preorderUtil(child);
            }
        }
    }
    public List<Integer> preorder(Node root) {
        preorderUtil(root);
        return ans;
    }
}