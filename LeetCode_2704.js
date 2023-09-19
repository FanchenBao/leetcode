/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    /*
    54 ms, faster than 43.01%
    */
    return {
        toBe: (otherVal) => {
            if (val === otherVal) {
                return true;
            }
            throw "Not Equal";
        },
        notToBe: (otherVal) => {
            if (val !== otherVal) {
                return true;
            }
            throw "Equal";
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */