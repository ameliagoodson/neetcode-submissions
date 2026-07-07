class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       # iterate through the characters 
       # strs[0] = base word
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

