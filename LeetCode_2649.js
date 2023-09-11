/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    /*
    Recursive generator in JavaScript requires "yield *".

    Ref: https://stackoverflow.com/a/32789830/9723036
    */
    for (const a of arr) {
        if (a instanceof Array) {
            yield * inorderTraversal(a);
        } else {
            yield a;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */