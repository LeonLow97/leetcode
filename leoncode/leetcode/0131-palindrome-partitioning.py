# 131 - https://leetcode.com/problems/palindrome-partitioning/

# Time: O(N * 2^N) where N is the length of string s
# Space: O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, subset = [], []

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return
            
            # include every possible substring
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True