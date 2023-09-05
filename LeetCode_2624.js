/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    // Not difficult, but requires some analysis. Treat the odd and even cols
    // differently in terms of the number of forward steps.
    // 175 ms, faster than 90.59%
    if (rowsCount * colsCount != this.length) {
        return [];
    }
    const res = [];
    let oddMoves = 2 * rowsCount - 1;
    let evenMoves = 1;
    for (let i = 0; i < rowsCount; i++) {
        res.push([this[i]]);
        let curIdx = i;
        for (let j = 1; j < colsCount; j++) {
            curIdx += j % 2 === 1 ? oddMoves : evenMoves;
            res[res.length - 1].push(this[curIdx])
        }
        oddMoves -= 2;
        evenMoves += 2;
    }
    return res;
}


Array.prototype.snail = function(rowsCount, colsCount) {
    // 194 ms, faster than 62.56%
    if (rowsCount * colsCount != this.length) {
        return [];
    }
    const res = new Array(rowsCount).fill(null).map(() => new Array(rowsCount).fill(null));
    for (let i = 0; i < rowsCount; i++) {
        for (let j = 0; j < colsCount; j++) {
            res[i][j] = j % 2 === 0 ? this[rowsCount * j + i] : this[rowsCount * j + rowsCount - i - 1];
        }
    }
    return res;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */