function factorial(num) {
  // base case (end the recursive function otherwise if goes on infinitely)
  if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(4));
console.log(factorial(0));
console.log(factorial(5));

// function factorial(num) {
//     let total = 1
//     for (let i = num; i > 1; i--) {
//         total *= i
//     }
//     return total
// }
