# 1832 - https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# Time: O(sentence)
# Space: O(1)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = sentence.lower().strip()
        unique = set()
        for char in sentence:
            if ord("a") <= ord(char) <= ord("z"):
                unique.add(char)
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for alphabet in alphabets:
            if alphabet not in unique:
                return False

        return True
