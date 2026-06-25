class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            if i == len(s) -1:
                return count
            else:
                count += abs(ord(s[i]) - ord(s[i+1]))
                print(abs(ord(s[i]) - ord(s[i+1])))
        
        return count

         