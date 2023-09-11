/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        let tExpired = false;
        const res = await Promise.race([
            new Promise((resolve) => setTimeout(() => {tExpired = true; resolve()}, t)),
            fn(...args),
        ]);
        if (tExpired) {
            throw "Time Limit Exceeded";
        }
        return res;
        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

var timeLimit = function(fn, t) {
    // Inspired by https://leetcode.com/problems/promise-time-limit/discuss/3413842/setTimeout-within-Promise-body
    return async function(...args) {
        // setTimeout is NON-BLOCKING!!!
        return new Promise((resolve, reject) => {
            const timeoutId = setTimeout(async () => {
                clearTimeout(timeoutId);
                reject("Time Limit Exceeded");
            }, t);
            fn(...args).then(resolve, reject);
        })
    }
};