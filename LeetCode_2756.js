/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */
var QueryBatcher = function(queryMultiple, t) {
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
        const resList = await this.queryMultiple(this.keys);
        for (let i in this.keys) {
            this.keyResolve[this.keys[i]](resList[i]);
        }
        this.keys = [];
        this.keyResolve = {};
        this.waiting = true;
        setTimeout(() => {
            this.waiting = false;
            this.getValue();
        }, this.t);
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