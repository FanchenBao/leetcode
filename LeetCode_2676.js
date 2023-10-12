/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    /*
    Feels a bit hacky. I think the official solution will be more elegant.
    
    69 ms, faster than 11.88%
    */
    let isThrottled = false;
    let latestArgs = null;
    
    const inner = function(...args) {
        if (isThrottled) {
            latestArgs = args;
        } else {
            if (latestArgs !== null) {fn(...latestArgs); latestArgs = null;}
            else fn(...args);
            
            isThrottled = true;
            setTimeout(() => {
                isThrottled = false;
                if (latestArgs !== null) inner(latestArgs);
            }, t);
        }
    }

    return inner;
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */