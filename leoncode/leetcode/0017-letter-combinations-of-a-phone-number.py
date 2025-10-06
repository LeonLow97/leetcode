# 17 - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Time: O(3^N * 4^M) - N is the number of digits mapping to 3 letters, M is the number of digits mapping to 4 letters
# Space: O(3^N * 4^M)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        digitsToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def dfs(i, word):
            if i >= len(digits):
                res.append(word)
                return

            chars = digitsToChar[digits[i]]
            for char in chars:
                dfs(i+1, word + char)
            
        dfs(0, "")
        return res
