/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
  let isCancelled = false;
  setTimeout(() => {

/**
 *  const result = [];
      if(!isCancelled)
          fn(...args);
  }, t);

  return () => {
    isCancelled = true;
  };
};
(
