/**
 * @param {Function} fn
 */
function memoize(fn) {
    // We passed, but with very bad performance. Need to get back on this later.
    // 7601 ms, faster than 10.37%

    const memo = {}
    const argsMap = {}

    return function(...args) {
        const argsMod = [];
        for (let i = 0; i < args.length; i++) {
            if (args[i] === undefined) {
                argsMod.push('undefined');
            } else {
                argsMod.push(args[i]);
            }
        }
        const key = JSON.stringify(argsMod);
        // console.log(key, memo, argsMap, key in memo);
        if (!(key in memo)) {
            memo[key] = fn(...args);
            argsMap[key] = [];
            argsMap[key].push(argsMod);
        } else {
            let hasMatch = false;
            for (const preArgs of argsMap[key]) {
                if (argsMod.every((a, i) => a === preArgs[i])) {
                    hasMatch = true;
                    break;
                }
            }
            if (!hasMatch) {
                fn(...args);
                argsMap[key].push(argsMod);
            }
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

/**
 * @param {Function} fn
 */
function memoize(fn) {
    // Use the Trie solution
    // Map is much more power than a regular object. Map can use
    // anything as its key, including objects, whereas an object
    // can only use String or Symbol as its keys.
    // E.g. const foo = new Map();
    // foo.set({}, 1);
    // foo.get({})  // undefined
    //
    // 303 ms, faster than 75.73%
    const root = new Map();

    return function(...args) {
        let node = root;
        for (const a of args) {
            if (!node.has(a)) {
                node.set(a, new Map());
            }
            node = node.get(a);
        }
        if (!node.has(NaN)) {
            // use NaN as the indicator of the end of a series of args
            node.set(NaN, fn(...args));    
        }
        return node.get(NaN);
    }
}