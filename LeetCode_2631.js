/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    // 118 ms, faster than 75.14%
    const res = {};
    for (const ele of this) {
        const key = fn(ele);
        if (!(key in res)) {
            res[key] = [];
        }
        res[key].push(ele);
    }
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

Array.prototype.groupBy = function(fn) {
    // 129 ms, faster than 46.40%
    return this.reduce((acc, cur) => {
        const key = fn(cur);
        if (!(key in acc)) {
            acc[key] = [];
        }
        acc[key].push(cur);
        return acc;
    }, {});
};