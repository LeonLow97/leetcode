# 937 - https://leetcode.com/problems/reorder-data-in-log-files/

# Time: O(N log N * L) where N is the number of logs, and L is the maximum length of a log.
# Space: O(N)

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