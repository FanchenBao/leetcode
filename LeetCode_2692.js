/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */
const handler = {
  set(obj, prop, value) {
    if (Array.isArray(obj)) {
        throw `Error Modifying Index: ${prop}`;
    } else {
        throw `Error Modifying: ${prop}`;
    }
  },
};

const DISABLED_FUNCS = ['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse'];

const disabled = (fname) => () => {throw `Error Calling Method: ${fname}`;};

var makeImmutable = function(obj) {
    /*
    Recursively make all objects in obj immutable. We use Proxy to trap any
    key or index modification. We directly set the array's mutation methods to
    throw error.

    439 ms, faster than 10.20%
    */
    if (Array.isArray(obj)) {
        for (let fname of DISABLED_FUNCS) {
            obj[fname] = disabled(fname);
        }
        for (let i = 0; i < obj.length; i++) {
            if (obj[i] !== null && typeof obj[i] === 'object') {
                obj[i] = makeImmutable(obj[i]);
            }
        }
    } else {
        for (let [key, val] of Object.entries(obj)) {
            if (val !== null && typeof val === 'object') {
                obj[key] = makeImmutable(val);
            }
        }
    }
    
    return new Proxy(obj, handler);
    
};

/**
 * const obj = makeImmutable({x: 5});
 * obj.x = 6; // throws "Error Modifying x"
 */


/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */
var makeImmutable = function(obj) {
    /*
    Inspired by the official solution. The tricks are two folds:
    
    1. Go through ALL the key-value pair, including the methods of array
    2. Trap the function call with the disabled name.
    
    403 ms, faster than 55.10%
    */
    const disabled = new Set(['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse']);

    const dfs = (o) => {
        if (typeof o === 'function') {
            return new Proxy(o, {
                apply: (func, thisArg, argList) => {
                    if (disabled.has(func.name)) {
                        throw `Error Calling Method: ${func.name}`;
                    }
                    return func.apply(thisArg, argList);
                }
            })
        }
        if (o === null || typeof o !== 'object') return o;
        if (Array.isArray(o)) {
            return new Proxy(o, {
                set: (_, prop) => {throw `Error Modifying Index: ${prop}`;},
                get: (_, prop) => dfs(o[prop]),
            });
        }
        return new Proxy(o, {
            set: (_, prop) => {throw `Error Modifying: ${prop}`;},
            get: (_, prop) => dfs(o[prop]),
        })
    }
    
    return dfs(obj);
    
};

/**
 * const obj = makeImmutable({x: 5});
 * obj.x = 6; // throws "Error Modifying x"
 */

