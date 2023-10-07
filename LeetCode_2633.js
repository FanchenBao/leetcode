/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    /*

    90 ms, faster than 19.87%
    */
    if (!object || typeof object !== 'object') {
        return typeof object === 'string' ? `"${object}"` : `${object}`;
    }
    if (Array.isArray(object)) {
        return '[' + object.map(obj => jsonStringify(obj)).join(',') + ']';
    }
    return '{' + Object.entries(object).map(([k, v]) => `"${k}":${jsonStringify(v)}`).join(',') + '}';
};