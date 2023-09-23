/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    // Cheating way, using Promise.all
    return Promise.all(functions.map(fn => fn()));
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */


/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    // This is completely from the official solution. The key take-home
    // point is that await is non-blocking (just like setTimeout). Thus,
    // we cna call await on an array of functions, without the forEach on
    // the array of functions being blocked. This creates an illusion of
    // parallelism.
    return new Promise((resolve, reject) => {
        if (functions.length === 0) {
            resolve([]);
            return;
        }
        const res = new Array(functions.length).fill(null);
        let numResolved = 0;
        functions.forEach(async (fun, idx) => {
            try {
                res[idx] = await fun();
                numResolved++;
                if (numResolved == functions.length) {
                    resolve(res);
                }
            } catch (e) {
                reject(e);
            }
        })
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */