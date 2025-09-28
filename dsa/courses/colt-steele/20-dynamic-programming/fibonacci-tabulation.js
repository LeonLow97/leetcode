function fib_tabulation(n) {
  if (n <= 2) return 1;
  var fibNums = [0, 1, 1];
  for (var i = 3; i <= n; i++) {
    fibNums[i] = fibNums[i - 1] + fibNums[i - 2];
  }
  return fibNums[n];
}

console.log("Result from Tabulation", fib_tabulation(10000));

function fib_memo(n, memo = []) {
  if (memo[n] !== undefined) return memo[n];
  if (n <= 2) return 1;
  var res = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
  memo[n] = res;
  return res;
}

// console.log(fib_memo(10000)); // returns an error: Maximum call stack size exceeded
try {
  fib_memo(10000);
} catch (error) {
  console.log("Result from Memoization");
  console.log(
    "RangeError: Maximum call stack size exceeded. Because Space Complexity of memoization is not as good as tabulation "
  );
}
