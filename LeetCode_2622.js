var TimeLimitedCache = function() {
    this.map = {};
};

TimeLimitedCache.prototype.isValid = function(key) {
    if (!(key in this.map) || new Date() - this.map[key][2] >= this.map[key][1]) {
        return false;
    }
    return true;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const curTime = new Date();
    const res = this.isValid(key);
    this.map[key] = [value, duration, new Date()];
    return res;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.isValid(key) ? this.map[key][0] : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    for (const key of Object.keys(this.map)) {
        if (!this.isValid(key)) {
            delete this.map[key];
        }
    }
    return Object.keys(this.map).length;
};



// Another solution using setTimeout and clearTimeout
// Ref: https://leetcode.com/problems/cache-with-time-limit/discuss/3406927/JavaScript-SHORT-and-SIMPLE-O(n)-solution-using-setTimeout


var TimeLimitedCache = function() {
    this.map = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const res = key in this.map;
    if (res) {
        clearTimeout(this.map[key][1]);
    }
    this.map[key] = [value, setTimeout(() => delete this.map[key], duration)];
    return res;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return (key in this.map) ? this.map[key][0] : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.map).length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
