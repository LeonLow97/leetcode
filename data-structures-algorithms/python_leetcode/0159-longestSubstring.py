'''
Difficulty: MEDIUM
No.159    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given a string s, find the length of the longest substring t that contains at most
2 distinct characters.
'''

def lengthOfLongestSubstringTwoDistinct(str):
    # base case
    if (len(str) < 3): return len(str)

    # define pointers
    start = 0
    end = 0
    maxLen = 0
    freqCounter = {}

    # define maxLen
    while (end < len(str)):
        
        if (str[end] not in freqCounter):
            freqCounter[str[end]] = 1
        else:
            freqCounter[str[end]] += 1

        # contract window if condition is not met
        while (len(freqCounter) > 2):
            freqCounter[str[start]] -= 1
            if (freqCounter[str[start]] == 0):
                # freqCounter.pop(str[start], None)
                del freqCounter[str[start]]
            start += 1

        maxLen = max(maxLen, end-start+1)
        end += 1
    
    return maxLen

print(lengthOfLongestSubstringTwoDistinct("eceba")) # 3 because t is "ece" which its length is 3
print(lengthOfLongestSubstringTwoDistinct("ccaabbb")) # 5
print(lengthOfLongestSubstringTwoDistinct("ee")) # 2
print(lengthOfLongestSubstringTwoDistinct("leon")) # 2

# Frequency Counter in Python
def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    return freq

my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# print(CountFrequency(my_list))