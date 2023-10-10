const flatten = (obj) => {
    const res = {};
    if (Array.isArray(obj)) {
        for (let i in obj) {
            if (!obj[i] || typeof obj[i] !== 'object') res[i] = obj[i];
            else {
                for (const [k, v] of Object.entries(flatten(obj[i]))) {
                    res[`${i}.${k}`] = v
                }
            }
        }
    } else {
        for (let k of Object.keys(obj)) {
            if (!obj[k] || typeof obj[k] !== 'object') res[k] = obj[k];
            else {
                for (const [kk, v] of Object.entries(flatten(obj[k]))) {
                    res[`${k}.${kk}`] = v
                }
            }
        }
    }
    return res;
}


/**
 * @param {Array} arr
 * @return {(string | number | boolean | null)[][]}
 */
var jsonToMatrix = function(arr) {
    /*
    The trick is to flatten an object into a mapping with a dot-concatenated key
    and its value.

    The rest is just grunt work to get the return value in the right shape.

    322 ms, faster than 43.48% 
    */
    const mxMap = {}; let flattened;
    for (let i = 0; i < arr.length; i++) {
        flattened = flatten(arr[i]);
        for (const [k, v] of Object.entries(flattened)) {
            if (!(k in mxMap)) {
                mxMap[k] = new Array(i).fill("");
            }
            mxMap[k].push(v);
        }
    }
    const sortedKeys = Object.keys(mxMap).sort();
    const res = [sortedKeys];
    for (let i = 0; i < arr.length; i++) {
        const row = [];
        for (let k of sortedKeys) {
            if (i < mxMap[k].length) row.push(mxMap[k][i]);
            else row.push("");
        }
        res.push(row);
    }
    return res;
};


const test = [{"a":{"b":1,"c":2,"d":{"e":5}}},{"a":{"b":3,"d":4}}];

console.log(jsonToMatrix(test))