<a href="https://cs.slides.com/colt_steele/built-in-data-structures-25">Built-in Data Structures Slides</a>

## Objects

- When to use objects?
    - When you **don't need order**
    - When you need fast access / insertion and removal.

|Objects|Big O|
|:-:|:-:|
|Insertion|O(1)|
|Removal|O(1)|
|Searching|O(N)|
|Access|O(1)|

- Searching has an O(N) time complexity because it has to go through the entire object to look for the `value` that we want.

|Object Methods|Big O|
|:-:|:-:|
|`Object.keys`|O(N)|
|`Object.values`|O(N)|
|`Object.entries`|O(N)|
|`hasOwnProperty`|O(1)|

- `hasOwnProperty` has time complexity of O(1) because it only looks for the keys, not values.

## Arrays

- When to use arrays?
    - When you need **order**
    - When you need fast access / insertion and removal (sort of ...).

|Arrays|Big O|
|:-:|:-:|
|Insertion|Insert at the end - O(1) <br> Insert at the beginning / middle - O(N)|
|Removal|Removing at the end - O(1) <br> Removing at the beginning / middle - O(N)|
|Searching|O(N)|
|Access|O(1)|

|Array Operations|Big O|
|:-:|:-:|
|`push`|O(1)|
|`pop`|O(1)|
|`shift`|O(N)|
|`unshift`|O(N)|
|`concat`|O(N)|
|`slice`|O(N)|
|`splice`|O(N)|
|`sort`|O(N * log N)|
|`forEach/map/filter/reduce/etc.`|O(N)|






