class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        
        for word in reversed(arr):
            if word != "":
                return len(word)