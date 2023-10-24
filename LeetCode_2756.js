/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */
var QueryBatcher = function(queryMultiple, t) {
    /*
    Definitely not the best implementation, but it works!
    */
    this.queryMultiple = queryMultiple;
    this.t = t;
    this.keyResolve = {};
    this.keys = [];
    this.waiting = false;
};

/**
 * @param {string} key
 * @return {Promise<string>}
 */
QueryBatcher.prototype.getValue = async function(key) {
    let retPromise;
    if (key !== undefined) {
        this.keys.push(key);
        let resolveFun;
        retPromise = new Promise((resolve) => resolveFun = resolve);
        this.keyResolve[key] = resolveFun;
    }
    if (!this.waiting && this.keys.length > 0) {
        const localKeys = [...this.keys]
        const localKeyResolve = {...this.keyResolve}
        this.waiting = true;
        this.keys = [];
        this.keyResolve = {};
        // schedule the timeout before calloing queryMultiple, such that we are
        // not wasting time waiting on both.
        setTimeout(() => {
            this.waiting = false;
            this.getValue();
        }, this.t);
        const resList = await this.queryMultiple(localKeys);
        for (let i in localKeys) {
            localKeyResolve[localKeys[i]](resList[i]);
        }
    }
    return retPromise;
};

/**
 * async function queryMultiple(keys) { 
 *   return keys.map(key => key + '!');
 * }
 *
 * const batcher = new QueryBatcher(queryMultiple, 100);
 * batcher.getValue('a').then(console.log); // resolves "a!" at t=0ms 
 * batcher.getValue('b').then(console.log); // resolves "b!" at t=100ms 
 * batcher.getValue('c').then(console.log); // resolves "c!" at t=100ms 
 */


/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */
var QueryBatcher = function(queryMultiple, t) {
    this.queryMultiple = queryMultiple;
    this.t = t;
    this.keyResolve = [];
    this.waiting = false;
};

/**
 * @param {string} key
 * @return {Promise<string>}
 */
QueryBatcher.prototype.getValue = async function(key) {
    let retPromise;
    if (key !== undefined) {
        // save the resolve in this.keyResolve, so that we can decide when
        // the returned promise is resolved
        retPromise = new Promise((resolve) => this.keyResolve.push({key, resolve}));
    }
    if (!this.waiting && this.keyResolve.length > 0) {
        // store the keyResolve in a local value, so that we can reset it.
        const localKeyResolve = this.keyResolve;
        this.waiting = true;
        this.keyResolve = [];
        setTimeout(() => {
            this.waiting = false;
            this.getValue();
        }, this.t);

        // Get the return values
        const resList = await this.queryMultiple(localKeyResolve.map(it => it.key));
        for (let i in resList) {
            localKeyResolve[i].resolve(resList[i]);
        }
    }
    return retPromise;
};

/**
 * async function queryMultiple(keys) { 
 *   return keys.map(key => key + '!');
 * }
 *
 * const batcher = new QueryBatcher(queryMultiple, 100);
 * batcher.getValue('a').then(console.log); // resolves "a!" at t=0ms 
 * batcher.getValue('b').then(console.log); // resolves "b!" at t=100ms 
 * batcher.getValue('c').then(console.log); // resolves "c!" at t=100ms 
 */