/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();
    for(const obj of arr1) map.set(obj.id, obj);
    for(const obj of arr2) {
        if(!map.has(obj.id)) map.set(obj.id, obj);
        else {
            const prevObj = map.get(obj.id);
            for(const key of Object.keys(obj)) prevObj[key] = obj[key];
        }
    }
    const res = new Array();
    for(let key of map.keys()) res.push(map.get(key));
    return res.sort((a,b)=>a.id-b.id); 
};
[{"id": 1,"x": 1},{"id": 2,"x": 9}]
[{"id": 3,"x": 5}]
[{"id": 1,"x": 2,"y": 3},{"id": 2,"x": 3,"y": 6}]
