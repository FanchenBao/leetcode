/**
 * @param {Function} fn
 */
function memoize1(fn) {
    // 318 ms, faster than 48.99%
    const memo = {}

    return function(...args) {
        const key = args.join(',');
        if (!(key in memo)) {
            memo[key] = fn(...args);    
        }
        return memo[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *   callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */


function memoize2(fn) {
    // use JSON.stringify to speed things up
    // 267 ms, faster than 93.80%
    const memo = {}

    return function(...args) {
        const key = JSON.stringify(args);
        if (!(key in memo)) {
            memo[key] = fn(...args);    
        }
        return memo[key];
    }
}