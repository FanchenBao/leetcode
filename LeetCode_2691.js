var ImmutableHelper = function(obj) {
    this.original = obj;
};

let mutated = false;

const getPartialClone = (ori, cur) => {
    // Collect the keys encountered by ori during get calls and set them in
    // cur. And set the value bound for ori in cur.
    return new Proxy(ori, {
        set(target, prop, value) {
            cur[prop] = value;
            mutated = true;
        },
        get(target, prop) {
            if (target[prop] !== null && typeof target[prop] === 'object') {
                if (cur[prop] === undefined) {
                    if (Array.isArray(target[prop])) {
                        cur[prop] = [];
                        for (let v of target[prop]) {
                            if (v === null || typeof v !== 'object') cur[prop].push(v);
                            else cur[prop].push(undefined);
                        }
                    } else {
                        cur[prop] = {};
                        for (let [k, v] of Object.entries(target[prop])) {
                            if (v === null || typeof v !== 'object') cur[prop][k] = v;
                            else cur[prop][k] = undefined;
                        }
                    }
                }
                return getPartialClone(target[prop], cur[prop]);
            }
            // we have to return cur[prop] if it is defined because a mutator
            // can mutate some value first and then use it. To accommodate this
            // we have to return the most up-to-date value.
            return cur[prop] === undefined ? Reflect.get(target, prop) : cur[prop];
        }
    });
}

/** 
 * @param {Function} mutator
 * @return {JSON} clone of obj
 */
ImmutableHelper.prototype.produce = function(mutator) {
    /*
    Fail.

    Very difficult for me. My idea was to record the chain of keys that results
    in a set action. However, since a set action can be preceded by multiple get
    actions, it is impossible to know which get action is the initiator of the
    set. And I was stuck on this approach.

    One correct approach is from https://leetcode.com/problems/immutability-helper/discuss/3544126/Confusing-Description

    In that method, we don't care about the chain of keys. We simply set the
    keys in the returning object (note, the returning object is not a copy of
    the orignal one, but merely contains the key-values that have been modified)
    that has been queried in the mutator callbacks. By doing this, we don't
    really care about which key is the initiator. We simply drill down the key
    chain along with the original object and record in the returning object all
    the keys that have been encountered. Eventually, when the set is called, we
    set the key-value in the returning object, not the original one.
    */
    let res = {};
    if (Array.isArray(this.original)) {
        res = [];
        for (let v of this.original) {
            if (v === null || typeof v !== 'object') res.push(v);
            else res.push(undefined);
        }
    } else {
        for (let [k, v] of Object.entries(this.original)) {
            if (v === null || typeof v !== 'object') res[k] = v;
            else res[k] = undefined;
        }
    }
    const p = getPartialClone(this.original, res);
    mutator(p);
    if (!mutated) res = this.original;
    mutated = false;
    console.log(res);
    return res;
};


// const originalObj = {"arr":[1,2,3]};
// const mutator = new ImmutableHelper(originalObj);

// const muts = [proxy => { proxy.arr[0] = 5; proxy.newVal = proxy.arr[0] + proxy.arr[1]; }];

// for (let mut of muts) {
//     const newObj = mutator.produce(mut);
//     // console.log(JSON.stringify(newObj));
//     console.log(newObj);
// }
