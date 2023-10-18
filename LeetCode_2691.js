var ImmutableHelper = function(obj) {
    this.original = obj;
    this.mutated = false;

    const getPartialClone = (ori, cur) => {
        // Collect the keys encountered by ori during get calls and set them in
        // cur. And set the value bound for ori in cur.

        const setTrap = (target, prop, value) => {
            if (target[prop] !== value) {
                cur[prop] = value;
                this.mutated = true;
            }
        }
        setTrap.bind(this);

        const getTrap = (target, prop) => {
            if (target[prop] !== null && typeof target[prop] === 'object') {
                if (cur[prop] === undefined) {
                    cur[prop] = {};
                }
                return getPartialClone(target[prop], cur[prop]);
            }
            // we have to return cur[prop] if it is defined because a mutator
            // can mutate some value first and then use it. To accommodate this
            // we have to return the most up-to-date value.
            return cur[prop] === undefined ? Reflect.get(target, prop) : cur[prop];
        }

        return new Proxy(ori, {set: setTrap, get: getTrap});
    }

    // this.foo = () => {
    //     const bar = () => {
    //         console.log(this.mutated);
    //     }
    //     bar.bind(this);
    //     bar();
    // };
};



const clone = (ori, pc) => {
    if (ori === null || typeof ori !== 'object' || typeof pc !== 'object') return pc;
    let res;
    if (Array.isArray(ori)) {
        res = [...ori];
        for (let [k, v] of Object.entries(pc)) {
            const idx = parseInt(k, 10);
            res[idx] = clone(ori[idx], v);
        }
    } else {
        res = {...ori};
        for (let [k, v] of Object.entries(pc)) {
            res[k] = clone(ori[k], v);
        }
    }
    return res;
}

/** 
 * @param {Function} mutator
 * @return {JSON} clone of obj
 */
ImmutableHelper.prototype.produce = function(mutator) {
    /*
    Fail.

    This solution is inspired by
    https://leetcode.com/problems/immutability-helper/discuss/3544126/Confusing-Description

    But it is different. The one from the forum does not work (probably the
    OJ has been improved such that those solutions no longer pass).

    The current solution first captures the chain of keys that leads to the
    modification of the value.

    Then we create a clone of the original object, BUT we don't have to expand
    on all the elements. We only expand on the keys that lead to the
    modification. All the other objects/arrays will be a shallow copy of the
    original, thus speeding up the cloning process.
    */
    const pc = {};
    mutator(getPartialClone(this.original, pc));
    const res = mutated ? clone(this.original, pc) : this.original;
    this.mutated = false;
    return res;
};

const originalObj = {"x": 5};
const mutator = new ImmutableHelper(originalObj);
const newObj = mutator.produce((proxy) => {
  proxy.x = proxy.x + 1;
});
// console.log(originalObj); // {"x: 5"}
// console.log(newObj); // {"x": 6}