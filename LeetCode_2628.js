/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // 68 ms, faster than 50.45%
    if (o1 === null && o2 === null) {return true;}
    if (o1 === null || o2 === null) {return false;}
    if (typeof o1 !== 'object' && typeof o2 !== 'object') {return o1 === o2;}
    if (typeof o1 === 'object' && typeof o2 === 'object') {
        if (Array.isArray(o1) && Array.isArray(o2)) {
            if (o1.length == o2.length) {
                return o1.every((e1, i) => areDeeplyEqual(e1, o2[i]));
            }
            return false;
        }
        if (!Array.isArray(o1) && !Array.isArray(o2)) {
            if (Object.keys(o1).length == Object.keys(o2).length) {
                return Object.keys(o1).every((k1) => areDeeplyEqual(o1[k1], o2[k1]))
            }
            return false;
        }
        return false;
    }
    return false;
};


/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
const replacer = (key, value) => {
    // See the documentation about the replacer function
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter
    if (value && typeof value === 'object' && !Array.isArray(value)) {
        return Object.fromEntries(Object.entries(value).sort());
    }
    return value;
}

var areDeeplyEqual = function(o1, o2) {
    // Official solution, leveraging JSON.stringify
    // If o1 and o2 are objects, sort it and then stringify them for comparison
    return JSON.stringify(o1, replacer) === JSON.stringify(o2, replacer);

}


/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    // Iterative approach
    // 79 ms, faster than 19.71%
    const stack = [[o1, o2]];
    while (stack.length > 0) {
        const [obj1, obj2] = stack.pop();
        if (obj1 === obj2) continue;
        if (typeof obj1 !== 'object' || typeof o2 !== 'object' || !obj1 || !obj2) return false;
        
        if (Array.isArray(obj1) !== Array.isArray(obj2)) return false;

        // obj1 and obj2 are both objects or both arrays. Treat them as objects
        // for comparison purpose
        if (Object.keys(obj1).length !== Object.keys(obj2).length) return false;
        for (let k in obj1) {
            stack.push([obj1[k], obj2[k]]);
        }
    }
    return true;
    
};