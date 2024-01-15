 * @param {Object|Array} obj
 * @return {Object}
 */
var invertObject = function(obj) {

    var result = {}
    for (const field in obj) {
        const resultFieldValue = result[obj[field]]
        if(!resultFieldValue) {
            result[obj[field]] = field
        } 
        else if(typeof resultFieldValue === "string") {
            result[obj[field]] = [result[obj[field]], field]
        } 
        else if (Array.isArray(resultFieldValue)) {
            result[obj[field]].push(field)
        }
    }
    return result
};
{
