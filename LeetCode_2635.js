/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // We can do it in place, but that's not the right way to implement Map
    // 55 ms, faster than 43.66%
    const res = [];
    for (let i = 0; i < arr.length; i++) {
        res.push(fn(arr[i], i));
    }
    return res;
};