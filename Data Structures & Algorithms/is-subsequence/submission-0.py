class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # loop through the longer one
        # pointer for s
        i = 0
        j = 0
        newStr = ""
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
            
        