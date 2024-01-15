var createObject = function(keysArr, valuesArr) {
    const obj = {};
    for (const i in keysArr) {
        if (!obj.hasOwnProperty(keysArr[i])) {
            obj[keysArr[i]] = valuesArr[i];
        }
    }
    return obj;
};
["a","b","c"]
[1,2,3]
[1,"1",false]
