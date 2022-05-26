/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let num = x
    rev = 0
    while (num > 0) {
        let las = num % 10
        rev = rev * 10 + las
        num = ~~(num/10)
    }
    return x == rev
};