/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let beg = 1
        let end = n
        while (beg <= end) {
            let mid = beg + ~~((end - beg) / 2)
            if (isBadVersion(mid - 1) == false && isBadVersion(mid) == true) {
                return mid
            }
            else if (isBadVersion(mid - 1) == false && isBadVersion(mid) == false) {
                beg = mid + 1
            }
            else if (isBadVersion(mid - 1) == true && isBadVersion(mid) == true) {
                end = mid - 1
            }
            else {
                mid += 0
            }
        }
    };
};