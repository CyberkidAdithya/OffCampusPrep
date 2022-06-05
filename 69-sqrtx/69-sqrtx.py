class Solution:
    def mySqrt(self, x: int) -> int:
        beg, end = 1, int(2e17)
        found = False
        while beg <= end:
            mid = beg + (end - beg) // 2	# to avoid mid overflow
            if mid ** 2 == x:				# condition
                found = True
                return mid	 				# found index
            elif mid ** 2 > x:
                end = mid - 1
            else:
                beg = mid + 1
        if not found:
            return beg if beg < end else end
        