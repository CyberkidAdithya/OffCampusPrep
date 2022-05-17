class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        w = ""
        while temp:
            w += str(temp.val)
            temp = temp.next
        return w == w[::-1]