/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => {
        const aValue = fn(a);
        const bValue = fn(b);
        
        if (aValue < bValue) return -1;
        if (aValue > bValue) return 1;
        return 0;
    });
};
