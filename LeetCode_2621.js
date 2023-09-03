/**
 * @param {number} millis
 */
async function sleep(millis) {
    /*
    53 ms, faster than 66.89%
    */
    return new Promise((resolve) => {
        setTimeout(() => resolve('foo'), millis);
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */