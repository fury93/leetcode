        // If property is null, return as is.
inheritance.
        prop === 'prototype' ||
    // 'get' trap creates a new proxy for nested objects or functions,
    // while returning primitive values and 'prototype' property as is.
    get : function(target, prop) {
      const condition =
        // 'prototype' property is returned as is to avoid potential issues with 
      throw Array.isArray(target) ? `Error Modifying Index: ${prop}` : `Error Modifying: $
{prop}`;
    },


  // Define the proxy handler object.
  const handler = {
    // 'set' trap throws an error when an attempt is made to modify a property.
    set : function(target, prop) {
var makeImmutable = function(obj) {
  // Define a set of methods that mutate the object or array.
  const methods = new Set(['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse']);
{"x":5}
(obj) => { obj.x = 5; return obj.x; }
[1,2,3]
