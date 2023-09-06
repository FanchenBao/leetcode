/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    // 53 ms, faster than 71.67% o
    let res = init;
    for (let n of nums) {
        res = fn(res, n);
    } 
    return res;
};