'''
Difficulty: MEDIUM
No.209    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Constraints:
- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50
'''

# Sliding Window Technique
def lengthOfLongestSubstringKDistinct(str, k):
    # define base case
    if (k == 0): return 0
    if (len(str) == 1): return 1

    # define pointers and frequency counter
    left = 0
    right = 0
    freqCounter = {}

    # define maxLen
    maxLen = 0

    # find maxLen of the longest substring with k distinct char
    while (right < len(str)):
        rightVal = str[right]

        # add the right values into the frequency counter
        if (rightVal in freqCounter):
            freqCounter[rightVal] += 1
        else:
            freqCounter[rightVal] = 1

        # check if frequency counter contains more items than k
        # contract window if we don't meet the condition
        while (len(freqCounter) > k):
            leftVal = str[left]
            freqCounter[leftVal] -= 1
            if (freqCounter[leftVal] == 0):
                del freqCounter[leftVal]
            left += 1
        
        # update maxLen
        maxLen = max(maxLen, right-left+1)
        right += 1
    
    return maxLen

print(lengthOfLongestSubstringKDistinct('eceba', 2)) # 3 "ece"
print(lengthOfLongestSubstringKDistinct('aa', 1)) # 2 "aa"
print(lengthOfLongestSubstringKDistinct('leon', 4)) # 4 "leon"