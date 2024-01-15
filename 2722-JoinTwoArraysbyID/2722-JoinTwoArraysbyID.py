    return obj2;
  }

  // Use the first object as the base for merging
  const res = obj1;

  // Iterate through the properties of obj2
  for (const key in obj2) {
    if (key in res) {
      // If the property exists in both, recursively merge them
  if (obj1 === null || obj2 === null) {
  // If either input is null, return obj2
  if (typeof obj1 !== 'object' || typeof obj2 !== 'object' || Array.isArray(obj1) !== Array.
isArray(obj2)) {
    return obj2;
  }


var deepMerge = function(obj1, obj2) {
  // If either input is not an object or their types differ (array vs. object), return obj2
{"a": 1, "c": 3}
{"a": 2, "b": 2}
[{}, 2, 3]
