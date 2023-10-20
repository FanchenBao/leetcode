/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */

const isObj = obj => obj !== null && typeof obj === 'object';

function objDiff(obj1, obj2) {
    /*
    Recursion. 63 ms, faster than 13.41%
    */
    if (!isObj(obj1) && !isObj(obj2)) {
        if (obj1 === obj2) return {};
        return [obj1, obj2];
    }
    if (isObj(obj1) && isObj(obj2)) {
        if (Array.isArray(obj1) && Array.isArray(obj2)) {
            const res = {};
            for (let i = 0; i < Math.min(obj1.length, obj2.length); i++) {
                if (obj1[i] !== undefined && obj2[i] !== undefined) {
                    const diff = objDiff(obj1[i], obj2[i]);
                    if (Object.keys(diff).length > 0) {
                        res[i] = diff;
                    }
                }
            }
            return res;
        }
        if (!Array.isArray(obj1) && !Array.isArray(obj2)) {
            const res = {};
            const keys = Object.keys(obj1).length > Object.keys(obj2).length ? Object.keys(obj2) : Object.keys(obj1);
            for (let k of keys) {
                if (k in obj1 && k in obj2) {
                    const diff = objDiff(obj1[k], obj2[k]);
                    if (Object.keys(diff).length > 0) {
                        res[k] = diff;
                    }
                }
            }
            return res;
        }
        return [obj1, obj2];
    }
    return [obj1, obj2];
};


/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */

const isObj = obj => obj !== null && typeof obj === 'object';

function objDiff(obj1, obj2) {
    /*
    Update: from the official solution, we realize that both array
    and object can be the argument of Object.keys. Thus, the operations
    on them can be unified.
    
    63 ms, faster than 13.41%
    */
    if (!isObj(obj1) && !isObj(obj2)) {
        if (obj1 === obj2) return {};
        return [obj1, obj2];
    }
    if (isObj(obj1) !== isObj(obj2) || Array.isArray(obj1) !== Array.isArray(obj2))
        return [obj1, obj2];

    // Both are objects or both are arrays
    const res = {}; let diff;
    for (let k of Object.keys(obj1)) {
        if (k in obj2) {
            diff = objDiff(obj1[k], obj2[k]);
            if (Object.keys(diff).length > 0)
                res[k] = diff;
        }
    }
    return res;
};