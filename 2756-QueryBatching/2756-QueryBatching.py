    }
    // If the batcher is not available, stash the query for later processing
    this.stashed.push({ key, resolve });
  });
};
};

QueryBatcher.prototype.getValue = function(key) {
  return new Promise((resolve) => {
    if (this.isAvailable) {
      this.isAvailable = false;
      this.queryMultiple([key]).then(results => resolve(results[0]));
      this.cooldown();  // Start the throttle time
      return;
var QueryBatcher = function(queryMultiple, t) {
  this.queryMultiple = queryMultiple;
  this.t = t;
  this.isAvailable = true;  // Flag to indicate if the batcher can immediately process a 
query
  this.stashed = [];  // Temporary storage for queries arriving during a throttle time
async function(keys) { return keys.map(key => key + '!'); }
100
[{"key": "a", "time": 10}, {"key": "b", "time": 20}, {"key": "c", "time": 30}]
