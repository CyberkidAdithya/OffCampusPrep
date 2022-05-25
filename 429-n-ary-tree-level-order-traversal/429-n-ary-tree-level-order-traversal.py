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
    List<List<Integer>> ans = new ArrayList<>();
    public List<List<Integer>> levelOrder(Node root) {
        if (root != null) {
            Queue<Node> que = new LinkedList<>();
            que.add(root);
            while (que.size() > 0) {
                int sz = que.size();
                List<Integer> sub = new ArrayList<>();
                for (int i = 0; i < sz; i++) {
                    Node curr = que.remove();
                    if (curr != null) {
                        sub.add(curr.val);
                        for (int j = 0; j < curr.children.size(); j++) {
                            que.add(curr.children.get(j));
                        }
                    }
                }
                ans.add(sub);
            }
        }
        return ans;
    }
}