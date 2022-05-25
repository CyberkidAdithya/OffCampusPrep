/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    hp = {}
    for (let i = 0; i < nums.length; i++) {
        hp[nums[i]] = 0;
    }
    ans = []
    for (let i = 0; i < nums.length; i++) {
        hp[nums[i]] +=1 ;
        console.log(Math.floor(nums.length/3))
        if (hp[nums[i]] > Math.floor(nums.length/3)) {
            ans.push(nums[i])
            hp[nums[i]] = -500000
        }
    }
    return ans;
};