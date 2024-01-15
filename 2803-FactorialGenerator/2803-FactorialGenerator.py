function* factorial(n) {
    if (n === 0) {
        yield 1;
    }
    let fact = 1;
    for (let i = 1; i <= n; i++) {
        fact *= i;

/**
 * const gen = factorial(2);
        yield fact;
    }
}
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
5
2
0
