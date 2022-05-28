import java.util.*;
class Solution {
    public int[] monotonicStack(int[] arr, int n) {
        Stack<Integer> stack = new Stack<Integer>();
        int[] nge = new int[n];
        for (int i = n - 1; i > -1; i--) {
            while ((stack.size() != 0) && (arr[i] >= arr[stack.peek()])) {
                stack.pop();
            }
            if (stack.size() == 0) {
                nge[i] = -1;
            } else {
                nge[i] = stack.peek();
            }
            stack.push(i);
        }
        return nge;
    }

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] greater = monotonicStack(nums2, nums2.length);
        for (int i = 0; i < nums2.length; i++) {
            if (greater[i] != -1) {
                greater[i] = nums2[greater[i]];
            }
        }
        HashMap<Integer, Integer> hp = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) {
            hp.put(nums2[i], greater[i]);
        }
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            ans[i] = hp.get(nums1[i]);
        }
        return ans;
    }
}