/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let ans = Array(nums.length * 2)
    for (let i = 0; i < nums.length; i++) {
        ans[i] = ans[i + nums.length] = nums[i]
    }
    return ans
};