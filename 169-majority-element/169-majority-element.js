/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    hp = {}
    for (let i = 0; i < nums.length; i++) {
        hp[nums[i]] = 0;
    }
    let ans = -1
    let maxx = -1
    for (let i = 0; i < nums.length; i++) {
        hp[nums[i]] +=1 ;
        if (hp[nums[i]] > maxx) {
            maxx = hp[nums[i]]
            ans = nums[i]
        }
    }
    return ans;
};