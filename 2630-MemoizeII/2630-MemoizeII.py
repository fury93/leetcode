      }
    } else {
      if (this.map.has(key)) {
        return this.map.get(key).getValueHelper(path, i + 1);
      } else {
        return { value: undefined, success: false };

  getValueHelper(path, i) {
    const key = path[i];
    if (i >= path.length) {
      if (this.hasValue) {
        return { value: this.value, success: true };
      } else {
        return { value: undefined, success: false };
class LookupTree {
  map = new Map();

  hasValue = false;

  value = null;
() => [[2,2],[2,2],[1,2]]
function (a, b) { return a + b; }
() => [[{},{}],[{},{}],[{},{}]]
