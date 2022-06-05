class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        beg, end = 0, len(arr) - 1
        found = False
        # return -1  
        while beg <= end:
            mid = beg + (end - beg) // 2	# to avoid mid overflow
            if mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    beg = mid + 1
            elif mid == n - 1:
                if arr[mid] > arr[mid - 1]:
                    return mid
                else:
                    end = mid - 1
            else:
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    if arr[mid - 1] > arr[mid]:
                        end = mid - 1
                    elif arr[mid + 1] > arr[mid]:
                        beg = mid + 1
                    else:
                        pass
            
                    
                