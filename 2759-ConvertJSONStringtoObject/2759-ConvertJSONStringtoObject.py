var undefinedToNull = function(obj) {
    if (obj === null || obj === undefined) return null;
    if (typeof obj !== 'object') return obj;
    if (Array.isArray(obj)) return obj.map(undefinedToNull);
    
    let res = {};
    for (let key in obj) {
        res[key] = undefinedToNull(obj[key]);
    }
    return res
};
{"a": undefined, "b":3}
{"a": undefined, "b":["a", undefined]}
