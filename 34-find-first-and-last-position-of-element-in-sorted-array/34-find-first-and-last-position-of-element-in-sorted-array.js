/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    pos1 = -1, pos2 = -1
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            pos1 = i
            break
        }
    }
    for (let i = nums.length - 1; i > -1; i--) {
        if (nums[i] == target) {
            pos2 = i
            break
        }
    }
    return [pos1, pos2]
};