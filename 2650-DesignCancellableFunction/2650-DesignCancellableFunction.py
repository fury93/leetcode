            } catch (e) {
                next = generator.throw(e);
            }
        }
                next = generator.next(await Promise.race([next.value, cancelPromise]));
    const promise = (async () => {
        let next = generator.next();
        while (!next.done) {
            try {
    var cancel;
    const cancelPromise = new Promise((_, reject) => { cancel = () => reject("Cancelled"); }
);
    // Every Promise rejection has to be caught.
    cancelPromise.catch(()=>{});

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
function*() { return 42; }
{"cancelledAt":100}
function*() { const msg = yield new Promise(res => res("Hello")); throw `Error: ${msg}`; }
