function sumRange(num) {
  if (num === 1) return 1;
  return num + sumRange(num - 1);
}

console.log(sumRange(3));

// in the first step, sumRange(2) is "waiting" because it doesn't have the value yet.
/* 
return 3 + sumRange(2)
                return 2 + sumRange(1)
                                1        
*/

// 3 + 3 = 6
