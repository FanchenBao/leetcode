/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // 62 ms, faster than 14.49% 
    const res = [];
    for (let i = 0; i < arr.length; i++) {
        if (Boolean(fn(arr[i], i))) {
            res.push(arr[i]);
        }
    }
    return res;
};


/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // In place, two pointers, but modify arr.
    // 50 ms, faster than 73.23%
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            arr[j] = arr[i];
            j++;
        }
    }
    return arr.slice(0, j);
};