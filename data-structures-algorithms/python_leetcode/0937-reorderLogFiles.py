'''
Difficulty: Medium
No.937    https://leetcode.com/problems/reorder-data-in-log-files/

You are given an array of logs. Each log is a space-delimited string of words, 
where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents 
are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''

from typing import List
from functools import cmp_to_key

# Eric Programming
# Time Complexity: O(n log n)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # separate the string by the identifier and the letter/digit log
        def splitStr(log: List[str]) -> List[str]:
            return log.split(' ', 1)
        
        # checking if the character (type 'str') is within the ASCII value of '0' and '9'
        def isNumber(char: str) -> bool:
            if char >= '0' and char <= '9':
                return True
            return False
        
        # comparator function
        def compare(a, b):
            if b < a: 
                return 1
            elif b > a: 
                return -1
            else:
                return 0
        
        def comparator(log1: str, log2: str) -> int:
            arr1 = splitStr(log1)
            arr2 = splitStr(log2)
            isNum1 = isNumber(arr1[1][0])
            isNum2 = isNumber(arr2[1][0])

            if isNum1 and isNum2:
                return 0
            elif isNum1:
                return 1
            elif isNum2:
                return -1
            
            isSameContent = arr1[1] == arr2[1]
            if isSameContent:
                return compare(arr1[0], arr2[0])
            return compare(arr1[1], arr2[1])
        
        return sorted(logs, key=cmp_to_key(comparator))

S = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(S.reorderLogFiles(logs)) # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(S.reorderLogFiles(logs)) # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]