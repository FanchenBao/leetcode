/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
  /*
  Use the theory from https://stackoverflow.com/a/67630963/9723036
  which states that the promise raced will continue to be executed.

  Use the trick from https://stackoverflow.com/a/42898229/9723036
  to identify which promise is the winner of the race.

  Then we can remove the winner from the current pool and add a new one to the
  pool.
  */
  const wrapper = async (f, k) => {
    const res = await f();
    return [res, k];
  }

  const map = Object.fromEntries(
    functions.slice(0, n).map(
      (f, i) => [i, wrapper(f, i)]
    )
  )
  
  let idx = n;
  const run = async () => {
    let res;
    while (Object.keys(map).length > 0) {
      console.log(map);
      const [cur, k] = await Promise.race(Object.values(map));
      delete map[k];
      res = cur;
      if (idx < functions.length) {
        map[idx] = wrapper(functions[idx], idx)
        idx++;  
      }
    }
    return res;
  }
  return run();
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */

functions = [
  () => new Promise(res => setTimeout(res('foo'), 3000)),
  () => new Promise(res => setTimeout(res('bar'), 4000)),
  () => new Promise(res => setTimeout(res('lol'), 2000)),
]
n = 2;


promisePool(functions, n).then();