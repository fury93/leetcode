Array.prototype.snail = function(rowsCount, colsCount) {
    if (this.length !==  rowsCount * colsCount) return [];
    
    let result = Array(rowsCount).fill(null).map(() => new Array(colsCount).fill(null));
    
    for (let j = 0; j < this.length; j++) {
        const i = Math.floor(j / rowsCount);
        
        if (i % 2 === 0) {
            result[j % rowsCount][i] = this[j];
            continue;
        }
        
        result[rowsCount - j % rowsCount - 1][i] = this[j];
    }
    return result;
}

[19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
5
4
