/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter1 = function(n) {
    // 52 ms, faster than 59.89%
    this.n = n;

    return function() {
        const res = this.n;
        this.n++;
        return res;
    };
};

var createCounter2 = function(n) {
    this.count = -1;

    return function() {
        this.count++;
        return this.count + n;
    };
};

var createCounter3 = function(n, count = [-1]) {
    // Use closure where the argument of createCounter is memorized by the
    // reutrn function. 39 ms, faster than 98.31%
    return function() {
        count[0]++;
        return count[0] + n;
    };
};

var createCounter4 = function(n, count = -1) {

    return function() {
        count++;
        return count + n;
    };
};


var createCounter5 = function(n) {
    let count = n - 1;

    return function() {
        return ++count;
    };
};

var createCounter6 = function(n) {
    return function() {
        return n++;
    };
};

var createCounter7 = function(n) {
    // This is the ULTIMATE version
    return () => n++;
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */