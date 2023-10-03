/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    /* Copied from https://leetcode.com/problems/design-cancellable-function/discuss/3440923/Simple-solution-with-async-and-Promise.race

    Not able to do anything about this. Completely clueless and have to rely on
    the discussion.

    This is adapted from the most voted. The use of Promise.race is brilliant,
    but the setup of cancelPromise is genius. Note that the cancelPromise does
    not resolve at all. Nor does it reject immediately. Instead, the power to
    reject cancelPromise is given to the cancel function. In other words, the
    cancelPromise is a never-resolved promise that can only be rejected
    immediately once the cancel function is called.

    When we race next.value and cancelPromise, as long as the cancel function is
    not called, next.value will always be the first to resolve or reject. If
    resolved, the resolved value gets passed back to the generator. Otherwise,
    the error gets thrown back to the generator, as well.

    Another piece of ingenuity is when cancel is called. The cancelPromise is
    rejected and most likley wins the race. The rejection gets caught in the
    function, and then the "Cancelled" string is thrown back to the generator.
    If generator.throw() does not throw another error, i.e., the "Cancelled"
    string gets caught in the generator code base, we continue the generation.
    However, if an error is thrown because of the "Cancelled" string,
    generator.throw() will throw the new error, which means the returned promise
    will reject by whatever that new error would be.

    I am not able to do write this, but I can sort of understand what the codes
    are doing.
    */
    var cancel;
    const cancelPromise = new Promise((_, reject) => { cancel = () => reject("Cancelled"); });

    const promise = (async () => {
        let next = generator.next();
        while (!next.done) {
            try {
                next = generator.next(await Promise.race([next.value, cancelPromise]));
            } catch (e) {
                next = generator.throw(e);
            }
        }
        return next.value;
    })();

    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */


var cancellable = function(generator) {
    /*
    This is my clumsy attempt 20 days after the initial copy-and-paste solution.
    It is definitely not as elegant, but it gets the job done (miraculously).

    */
    // Create the cancel function. When the cancel function is called,
    // the cancelPromise gets rejected.
    let rejectFun;
    const cancelPromise = new Promise((_, reject) => {
        rejectFun = reject;
    });
    const cancel = () => rejectFun('Cancelled');
    
    // Handle the generator
    let res;
    let val;
    
    const promiseFun = async () => {
        res = generator.next()
        while (true) {
            try {
                val = await Promise.race([res.value, cancelPromise]);
                if (res.done) {
                    break;
                }
                res = generator.next(val);
            } catch (err) {
                res = generator.throw(err);
            }
        }
        return val;
    };
    
    return [cancel, promiseFun()];
};
