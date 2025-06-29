function numberCompare(num1, num2) {
  // return num1 - num2  // sorting from smallest to largest
  return num2 - num1; // sorting from largest to smallest
}

let numArr = [4, 1, 6, 10, 3, 17];
console.log(numArr.sort(numberCompare));

function compareByLen(str1, str2) {
  //   return str1.length - str2.length;
  return str2.length - str1.length;
}

let strArr = ["Jie Wei", "Leon", "Data Structures", "Algorithms"];
console.log(strArr.sort(compareByLen));
