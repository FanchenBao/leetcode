/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    /*
    1088 ms, faster than 5.01% 
    */
    if (!(obj instanceof Object)) {
        return obj;
    }
    if (obj instanceof Array) {
        for (let i = obj.length - 1; i >= 0; i--) {
            if (!Boolean(obj[i])) {
                obj.splice(i, 1);
            } else {
                obj[i] = compactObject(obj[i]);
            }
        }
    } else {
        for (const k of Object.keys(obj)) {
            if (!Boolean(obj[k])) {
                delete obj[k];
            } else {
                obj[k] = compactObject(obj[k])
            }
        }
    }
    
    return obj;
};


/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    /*
    Iterative approach.

    The official solution points out the downside of using recursion, because it
    relies on the callstack, which might lead to stack overflow if the nesting of
    obj is deep.
    */
    const stack = [[obj, null, null]]
    while (stack.length > 0) {
        let [curObj, parObj, parIdx] = stack.pop();
        if (!(curObj instanceof Object)) {
            continue;
        }
        if (curObj instanceof Array) {
            for (let i = curObj.length - 1; i >= 0 ; i--) {
                if (!Boolean(curObj[i])) {
                    curObj.splice(i, 1)   
                }
            }
            for (let i = 0; i < curObj.length; i++) {
                stack.push([curObj[i], curObj, i]);
            }
        } else {
            for (const k of Object.keys(curObj)) {
                if (!Boolean(curObj[k])) {
                    delete curObj[k];
                } else {
                    stack.push([curObj[k], curObj, k]);
                }
            }
        }
        if (parIdx !== null) {
            parObj[parIdx] = curObj;    
        }
    }
    return obj;
};