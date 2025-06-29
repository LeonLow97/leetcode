function collectOdd(arr) {
  let newArr = [];

  // base case
  if (arr.length === 0) {
    return newArr;
  }

  if (arr[0] % 2 !== 0) {
    newArr.push(arr[0]);
  }

  newArr = newArr.concat(collectOdd(arr.slice(1)));

  return newArr;
}

console.log(collectodd([1, 2, 3, 4, 5]));

/*
[1].concat(collectOdd([2,3,4,5]))
            [].concat(collectOdd([3,4,5]))
                        [3].concat(collectOdd([4,5]))
                                    [].concat(collectOdd([5]))
                                                [5].concat(collectOdd([]))
*/
