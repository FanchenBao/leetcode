Array.prototype.last = function() {
    /*
    LeetCode 2619

    Use "this" to access an instance of Array
    */
    if (this.length == 0) {
        return -1;
    }
    return this[this.length - 1];
};