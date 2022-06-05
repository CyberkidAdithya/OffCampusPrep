class Solution:
    def search(self, arr: List[int], key: int) -> int:
        beg, end = 0, len(arr) - 1
        found = False
        while beg <= end:
            mid = beg + (end - beg) // 2	# to avoid mid overflow
            if key == arr[mid]:				# condition
                found = True
                return mid	 				# found index
            elif key < arr[mid]:
                end = mid - 1
            else:
                beg = mid + 1
        if not found:
            return -1