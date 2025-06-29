# Deque in Python

- Deque (Doubly Ended Queue) is preferred over _list_ in the cases where we need quicker append and pop operations from both ends of the container as deque provides an **O(1) time complexity** for append and pop operations as compared to a list that provides O(N) time complexity.

```py
from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])

print(Queue)
```

- Output

```
deque(['name', 'age', 'DOB'])
```

## Appending Items Efficiently

- `append()`: used to insert the value in its argument to the right end of the deque.
- `appendleft()`: used to insert the value in its argument to the left end of the deque.

```py
# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)
```

- Output

```
deque:  deque([1, 2, 3])

The deque after appending at right is :
deque([1, 2, 3, 4])

The deque after appending at left is :
deque([6, 1, 2, 3, 4])
```

## Popping Items Efficiently

- `pop()`: used to delete an argument from the right end of the deque.
- `popleft()`: used to delete an argument from the left end of the deque.

```py
# importing "collections" for deque operations
import collections
 
# initializing deque
de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)
 
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
 
# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)
 
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
 
# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)
```

- Output

```
deque:  deque([6, 1, 2, 3, 4])

The deque after deleting from right is : 
deque([6, 1, 2, 3])

The deque after deleting from left is : 
deque([1, 2, 3])
```

## Complexity Analysis

| Methods        | Time Complexity | Auxiliary Space |
| -------------- | --------------- | --------------- |
| `append()`     | O(1)            | O(1)            |
| `appendleft()` | O(1)            | O(1)            |
| `pop()`        | O(1)            | O(1)            |
| `popleft()`    | O(1)            | O(1)            |
