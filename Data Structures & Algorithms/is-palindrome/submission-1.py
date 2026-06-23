class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        emptyStr = ""

        for char in s:
            if char.isalnum():
                emptyStr += char.lower()
        
        return emptyStr == emptyStr[::-1]
       

        