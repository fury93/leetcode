
    const res = new Array(functions.length).fill(null);
    let settledCounter = 0;

    const updateResultAndCheckResolve = (result, idx) => {
      res[idx] = result;
      settledCounter++;
      if(settledCounter === functions.length) resolve(res);
    };

    functions.forEach((func, idx) => {
      func().then(subRes => {
        updateResultAndCheckResolve({status: 'fulfilled', value: subRes}, idx);
      }, err => {
      return;
    }
  return new Promise(resolve => {
    if(functions.length === 0) {
      resolve([]);
var promiseAllSettled = function(functions) {
[() => new Promise(resolve => setTimeout(() => resolve(15), 100))]
[() => new Promise(resolve => setTimeout(() => resolve(20), 100)), () => new Promise(resolve => setTimeout(() => resolve(15), 100))]
[() => new Promise(resolve => setTimeout(() => resolve(30), 200)), () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100)
