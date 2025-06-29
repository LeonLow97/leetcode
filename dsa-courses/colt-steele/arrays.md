# Array Methods Summary (JavaScript)

|      Method       |                                            Description                                            |
| :---------------: | :-----------------------------------------------------------------------------------------------: |
|    `splice()`     |                  Adds/Removes array elements and overwrites the original array.                   |
|    `indexOf()`    | Returns the first index at which a given element can be found in the array, or -1 if not present. |
|     `slice()`     |                     Returns the selected elements in an array as a new array                      |
| `Array.isArray()` |                    Returns `true` if an object is an array, otherwise `false`.                    |

## `splice()`

- `splice()` method adds and/or removes array elements.
- `splice()` method overwrites the original array.
- Syntax:

```js
array.splice(index, howmany, item1, ..., itemX)
```

## `indexOf()`

- The `indexOf()` method returns the first index at which a given element can be found in the array, or -1 if it is not present.
- `indexOf()` is case sensitive.
- `indexOf()` is another loop --> **Adds O(N) time complexity.**
- Syntax:

```js
string.indexOf(searchvalue, start_position);
```

## `slice()`

## `Array.isArray()`
