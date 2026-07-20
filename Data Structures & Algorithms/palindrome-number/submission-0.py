class Solution:
    def isPalindrome(self, x: int) -> bool:
        stri = str(x)
        l, r = 0, len(stri)-1

        while l < r:
            if stri[l] != stri[r]:
                return False
            l += 1
            r -= 1
        return True