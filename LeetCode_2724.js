/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    /*
    138 ms, faster than 18.22%
    */
    return arr.sort((a, b) => fn(a) - fn(b));
};