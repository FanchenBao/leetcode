const getProto = (obj) => {
    if (obj === null) {
        return new Set();
    }
    const propSet = new Set(Object.getOwnPropertyNames(obj));
    for (const p of getProto(Object.getPrototypeOf(obj))) {
        propSet.add(p);
    }
    return propSet;
};

var checkIfInstanceOf1 = function(obj, classFunction) {
    /*
    This is hard for me. The idea here is that we first conduct bunch of checks.
    Then we obtain all the prototype of classFunction, including all the
    inherited ones. Then we add a dummy method to it.

    Then we get all the prototype of obj. If every key from the classFunction's
    prototype is in the obj's prototype, including the dummy method, obj is an
    instance of classFunction.

    98 ms, faster than 60.63%
    */
    if (obj === undefined || obj === null || classFunction === undefined || classFunction === null || classFunction.prototype === undefined) {
        // check null or undefined, and check whether classFunction is indeed a Class
        return false;
    }
    const classProto = getProto(classFunction.prototype);
    // add a dummy prototype to class
    let dummyName;
    while (true) {
        dummyName = Math.random().toString().slice(0, 3);
        if (!classProto.has(dummyName)) {
            classFunction.prototype[dummyName] = () => {};
            classProto.add(dummyName);
            break;
        }
    }
    const objProto = getProto(obj);
    // objProto must contain everything from classProto
    let res = true;
    for (const p of classProto) {
        if (!objProto.has(p)) {
            res = false;
            break;
        }
    }
    delete classFunction.prototype[dummyName];
    return res;
};


var checkIfInstanceOf2 = function(obj, classFunction) {
    // Solution from https://leetcode.com/problems/check-if-object-instance-of-class/discuss/3406546/Basic-JavaScript-Solution-oror-Easy-to-understand-oror-beginner-friendly/1862208
    // Get the classFunction's prototype.
    // Then traverse the prototype chain of the object. Whenever one level of
    // prototype in the chain matches the classFunction's prototype, we have an
    // instanceOf match.
    // 91 ms, faster than 82.12% 
    const prototype = classFunction?.prototype;
    while (obj !== null && obj !== undefined) {
        obj = Object.getPrototypeOf(obj);
        if (obj === prototype) return true;
    }
    return false;
};
