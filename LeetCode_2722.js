/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    /*
    What the heck! JavaScript default to sort on unicode value, which for
    numbers means that it defaults sort on the string version of the number.
    We must explicitly tell the sort function to sort based on numerical
    comparsion.

    I have to go back and check all the code in my react native project.

    354 ms, faster than 25.60%
    */
    const map = {};
    for (const ele of arr1) {
        map[ele.id] = {...map[ele.id], ...ele};
    }
    for (const ele of arr2) {
        map[ele.id] = {...map[ele.id], ...ele};
    }
    return Object.keys(map).sort((a, b) => parseInt(a) - parseInt(b)).map(k => map[k]);
};


// const arr1 = [{"id":0,"c":49,"y":82,"z":88,"x":15,"m":73,"i":70,"s":42,"q":4},{"id":2,"q":34,"o":25,"u":22,"v":18,"w":66,"j":99,"g":20},{"id":3,"h":39,"b":6,"j":12,"q":53,"v":33,"y":79,"c":61,"x":12,"k":94,"s":40},{"id":5,"q":66,"n":46,"u":4,"w":30,"x":4,"b":43},{"id":7,"y":14,"e":39,"f":34,"z":78,"j":64,"o":90},{"id":8,"l":64,"x":60,"g":34,"n":67,"m":97,"i":80,"b":11},{"id":9,"u":87,"b":71,"i":37,"r":24,"s":51},{"id":10,"n":52,"f":86,"c":60,"b":13},{"id":11,"t":78,"y":80,"i":7,"w":80,"s":64,"m":49,"o":21},{"id":12,"p":59,"j":82,"k":27,"i":24,"v":16,"t":12,"x":92},{"id":14,"f":2,"t":91,"k":32,"z":15,"x":39,"h":80,"o":52},{"id":15,"i":42,"r":45,"v":70,"g":36,"a":86,"u":69,"s":0,"m":13},{"id":17,"l":0,"z":11,"u":66,"c":67,"t":58,"w":60,"m":45,"f":4},{"id":18,"i":0,"t":79,"m":1,"h":29,"n":76,"z":11,"k":57,"f":63},{"id":19,"n":30,"e":20,"p":69,"m":42,"l":7,"s":21},{"id":20,"d":78,"y":77,"w":0},{"id":21,"p":55,"c":47,"z":4,"q":70,"j":43,"w":33},{"id":23,"h":51,"w":44,"u":13,"d":52,"c":90,"i":81}];
// const arr2 = [{"id":0,"q":2,"m":50,"r":94,"o":34,"w":11,"h":82,"t":7,"z":64},{"id":2,"z":94,"y":3},{"id":3,"n":29,"h":50,"q":16},{"id":5,"j":64,"l":57,"g":52,"v":94,"k":1,"i":76,"b":50},{"id":7,"y":88,"u":42,"o":24},{"id":8,"p":74,"w":28,"d":66,"x":6,"a":63,"n":34,"k":63,"s":99,"e":20},{"id":10,"u":25,"r":2},{"id":11,"u":27,"p":62},{"id":13,"i":61,"w":78,"o":84},{"id":15,"n":57,"m":99,"z":38},{"id":16,"h":22,"r":98,"i":53},{"id":17,"j":5,"n":51,"l":49,"a":9,"z":44,"s":54,"p":61,"v":10,"y":9},{"id":18,"l":31,"m":10,"s":28,"a":71,"d":17,"b":27},{"id":20,"g":34,"b":45,"i":66},{"id":21,"t":95,"k":49,"y":68},{"id":22,"l":92,"s":7,"q":83},{"id":23,"n":19,"b":50,"m":72,"k":10,"z":20},{"id":25,"r":41,"e":45,"c":69,"y":97,"x":43,"n":52}];
// join(arr1, arr2);