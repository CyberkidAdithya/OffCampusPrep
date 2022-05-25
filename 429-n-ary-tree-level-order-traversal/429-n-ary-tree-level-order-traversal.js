/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    ans = []
    if (root) {
        que = []
        que.push(root)
        while (que.length > 0) {
            console.log(que.length)
            sub = []
            let sz = que.length
            for (let i = 0; i < sz; i++) {
                let curr = que.shift()
                if (curr != null) {
                    sub.push(curr.val)
                    if (curr.children)
                        que.push(...curr.children) 
                }
            }
            console.log(sub)
            ans.push(sub)
        }
        let anss = [...ans,...ans]
        console.log(anss)
    }
    return ans
}