class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shashmap = {}
        thashmap = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in shashmap:
                shashmap[s[i]] = 1
            else:
                shashmap[s[i]] += 1
            
            if t[i] not in thashmap:
                thashmap[t[i]] = 1
            else:
                thashmap[t[i]] += 1
        print(shashmap)
        print(thashmap)
        
        return shashmap == thashmap

