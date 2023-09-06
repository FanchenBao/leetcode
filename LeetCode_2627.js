/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    /*
    No special trick needed. Each time the function is called, we simply clear
    out the previous timeout. If the previous timeout has been completed, no
    harm done. Otherwise, we cancel it and set up a new timeout.

    56 ms, faster than 71.15% 
    */
    let timeoutId;

    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */