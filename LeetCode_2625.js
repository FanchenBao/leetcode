/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    /*
    Very difficult to understand what the question is asking about. Each nested
    array has its depth and it starts with 0. If its depth is smaller than n,
    the array gets flattened. Otherwise, it stays as is.

    We use recursion to check each nested array. As long as the current array's
    depth is larger or equal to n, all other nested arrays inside will also not
    be subject to flatten.

    Another trick here is that in the recursion function, when an array is not
    flattened, we wrap another array on top of it.

    118 ms.
    */
    
    function helper(arr, depth) {
        if (depth >= n) {
            return [arr]; // no flatten
        }
        const res = []; // flatten by not wrapping another array outside
        for (const a of arr) {
            if (a instanceof Array) {
                for (const b of helper(a, depth + 1)) {
                    res.push(b);
                }
            } else {
                res.push(a);
            }
        }
        return res;
    }

    return helper(arr, -1);
};


var flat = function (arr, n) {
    /*
    Very smart solution: https://leetcode.com/problems/flatten-deeply-nested-array/discuss/3983510/JavaScript-solution-using-Recursion-oror-Easiest-Solution-!!!

    Use a "global" res to hold the flattened array.

    Then during recursion, flattening is achieved by directly pushing values to
    the global res. Imagine we can go multiple nesting array deep, but if they
    need to be flattened, their values all go directly to the global res, hence
    flattened.

    O(N), 95 ms, faster than 88.31%
    */
    const res = []
    
    function helper(arr, depth) {
        for (const ele of arr) {
            if (ele instanceof Array && depth < n) {
                helper(ele, depth + 1);
            } else {
                res.push(ele);
            }
        }
        return res;
    }

    return helper(arr, 0);
};