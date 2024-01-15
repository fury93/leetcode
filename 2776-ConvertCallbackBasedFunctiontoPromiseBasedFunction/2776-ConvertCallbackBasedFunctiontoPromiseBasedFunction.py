var promisify = (fn) => async (...args) =>
  new Promise((resolve, reject) =>
    fn((data, err) => err ? reject(err) : resolve(data), ...args)
  );

(callback, a, b, c) => { callback(a * b * c) }
[1, 2, 3]
(callback, a, b, c) => { callback(a * b * c, "Promise Rejected") }
