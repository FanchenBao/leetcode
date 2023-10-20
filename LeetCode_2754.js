/**
 * @param {Object} obj
 * @return {Function}
 */
Function.prototype.bindPolyfill = function(obj) {
    /*
    This article helps explain what apply (and call, for that matter)
    does. https://www.freecodecamp.org/news/understand-call-apply-and-bind-in-javascript-with-examples/
    
    The apply (and call) method takes the first argument as the context
    of the function.
    */
    const f = (...args) => this.apply(obj, args);
    return f;
}