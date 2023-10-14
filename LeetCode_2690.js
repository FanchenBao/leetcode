/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    /*
    Learned about Proxy!

    41 ms, faster than 93.80% 
    */
    const handler = {
        get: (target, prop, receiver) => {
            return () => prop;
        }
    }
    return new Proxy({}, handler);
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */