/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    return new Proxy({}, {
};

/**
 * const obj = createInfiniteObject();
        get: (_, prop)=> () => prop
    });
 * obj['abc123'](); // "abc123"
 */
"
