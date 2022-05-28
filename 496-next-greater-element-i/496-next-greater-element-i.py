class Solution:
    def monotonicstack(self, arr, n):
        stack = []  # monotonic stack
        nge = [0] * n
        for i in range(n - 1, -1, -1):
            while stack != [] and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack == []:
                nge[i] = -1
            else:
                nge[i] = stack[-1]
            stack.append(i)
        return nge
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.monotonicstack(nums2, len(nums2))
        # print(greater)
        greater = [nums2[greater[i]] if greater[i] != -1 else -1 for i in range(len(nums2))]
        
        # print(greater)
        # print(nums2)
        hp = dict(zip(nums2, greater))
        print(hp)
        
        ans = [hp[nums1[i]] for i in range(len(nums1))]
        return ans