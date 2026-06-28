class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # strip all numbers and white spaces in new string
        string = ""

        for char in s:
            if char.isalnum():
                string += char.lower()

        print(string)
        return string == string[::-1]