class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def mts(a, b = '0'):
            if b == '0' or a == b:
                return 0
            elif a > b:
                return 1
            else:
                return -1
        prevsign = mts(*arr[:2])
        localmax = globalmax = 2 if prevsign else 1
        for i in range(1, len(arr) - 1):
            currsign = mts(arr[i], arr[i + 1])
            if currsign == 0:
                localmax = 1
            elif currsign == prevsign:
                localmax = 2
            else:
                localmax += 1
            prevsign = currsign
            globalmax = max(globalmax, localmax)
        return globalmax