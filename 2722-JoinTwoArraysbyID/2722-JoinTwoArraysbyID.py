
Function.prototype.bindPolyfill = function(obj) {
  const self = this;  // Reference to the original function using closure

  return function(...args) {     // Return a new function
    return self.apply(obj, args);  // Invoke original function with obj context using apply
  }
}

function f(multiplier) { return this.x * multiplier; }
{"x":10}
[5]
