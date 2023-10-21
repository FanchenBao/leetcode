/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
isObj = obj => obj !== undefined && obj !== null && typeof obj === 'object';

var deepMerge = function(obj1, obj2) {
    /*
    The situation where we return obj2 is:
    
    - obj1 and obj2 are neither objects
    - one of obj1 and obj2 is not object
    - one of obj1 and obj2 is array and the other is object
    */
    if (!isObj(obj1) && !isObj(obj2) || isObj(obj1) !== isObj(obj2) || Array.isArray(obj1) !== Array.isArray(obj2))
        return obj2;
    if (Array.isArray(obj2)) {
        const res = [];
        for (let i = 0; i < obj2.length; i++)
            res[i] = deepMerge(obj1[i], obj2[i]);
        for (let i = obj2.length; i < obj1.length; i++)
            res[i] = obj1[i];
        return res;
    }
    const res = {};
    const keySet = new Set(Object.keys(obj1));
    for (let k of Object.keys(obj2)) {
        res[k] = deepMerge(obj1[k], obj2[k]);
        keySet.delete(k);
    }
    for (let k of keySet) res[k] = obj1[k];
    return res;

};

/**
 * let obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2};
 * deepMerge(obj1, obj2); // {"a": 2, "c": 3, "b": 2}
 */


/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
isObj = obj => obj !== undefined && obj !== null && typeof obj === 'object';

var deepMerge = function(obj1, obj2) {
    /*
    Better implementation from https://leetcode.com/problems/deep-merge-of-two-objects/discuss/3807283/Simple-yet-intuitive-solution

    100 ms, faster than 64.18% 
    */
    if (!isObj(obj1) && !isObj(obj2) || isObj(obj1) !== isObj(obj2) || Array.isArray(obj1) !== Array.isArray(obj2))
        return obj2;
    const res = obj1;
    for (let k in obj2) {
        if (k in obj1) res[k] = deepMerge(obj1[k], obj2[k]);
        else res[k] = obj2[k];
    }
    return res;

};

/**
 * let obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2};
 * deepMerge(obj1, obj2); // {"a": 2, "c": 3, "b": 2}
 */

