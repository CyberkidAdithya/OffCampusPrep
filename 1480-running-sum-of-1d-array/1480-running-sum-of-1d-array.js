/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let summ = 0
    let ans = Array(nums.length)
    for (let i = 0; i < nums.length; i++) {
        summ += nums[i]
        ans[i] = summ
    }
    return ans
};