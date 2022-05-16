class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num:
            arr.append(num % 10)
            num //= 10
        arr.sort()
        num1 = arr[0] * 10 + arr[2]
        num2 = arr[1] * 10 + arr[3]
        return num1 + num2