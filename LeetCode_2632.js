/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    /*
    The key to solving this problem is to know that in javascript,
    function.length is the number of arguments the function will take.
    See: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length
    */
    const curriedArgs = [];
    
    return function curried(...args) {
        for (const a of args) {
            curriedArgs.push(a);
        }
        if (curriedArgs.length === fn.length) {
            return fn(...curriedArgs);
        }
        return curried;
    }
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */

// function sum(a, b) { return a + b; }
const sum = (a, b) => a + b;
console.log(sum.length)
curry(sum)