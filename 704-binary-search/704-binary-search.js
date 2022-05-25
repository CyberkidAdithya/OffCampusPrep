/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let beg = 0, end = nums.length - 1
    while (beg <= end) {
        mid = beg + ~~((end - beg) / 2)
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target) {
            beg = mid + 1
        }
        else {
            end = mid - 1
        }
    }
    return -1;
};