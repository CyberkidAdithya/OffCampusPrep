typedef long long int ll;
class Solution {
public:
    bool isPalindrome(int x) {
        int rev = 0;
        int num = x;
        while (num > 0) {
            int las = num % 10;
            rev = (ll)rev * 10 + las;
            num /= 10;
        }
        return x == rev;
    }
};