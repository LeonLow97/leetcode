function fib(n, memo = []) {
  if (memo[n] !== undefined) return memo[n];
  if (n <= 2) return 1;
  var res = fib(n - 1, memo) + fib(n - 2, memo);
  memo[n] = res;
  return res;
}

console.log(fib(10));
console.log(fib(20));
console.log(fib(30));
console.log(fib(40));
console.log(fib(50));
console.log(fib(100));

// Another shorter solution
// function fib(n, memo = [undefined, 1, 1]) {
//     if (memo[n] !== undefined) return memo[n];
//     var res = fib(n - 1, memo) + fib(n - 2, memo);
//     memo[n] = res;
//     return res;
//   }
