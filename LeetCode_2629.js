/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose1 = function(functions) {
    // Go right to left
    // 60 ms, faster than 81.69% 
    return function(x) {
        let res = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            res = functions[i](res);
        }
        return res;
    }
};


var compose2 = function(functions) {
    // recursion
    // 58 ms, faster than 87.46%
    return function(x) {

        const helper = (arg, idx) => {
            if (idx == functions.length) {
                return arg;
            }
            return functions[idx](helper(arg, idx + 1));
        }
    
        return helper(x, 0);
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */