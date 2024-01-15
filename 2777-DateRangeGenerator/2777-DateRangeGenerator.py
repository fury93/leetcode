/**
 * @param {string} start
 * @param {string} end
 * @param {number} step
 * @yields {string}
 */
var dateRangeGenerator = function* (start, end, step) {
    const startDate = new Date(start);
    const endDate = new Date(end);

    while (startDate <= endDate) {
        yield startDate.toISOString().split('T')[0].trim();
        startDate.setDate(startDate.getDate() + step);
    }
};
"2023-04-01"
"2023-04-04"
1
