class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1

        while l < r:
            temp = s[l]
            s[l] = s[r] # set left to right
            s[r] = temp # set right to left
            l +=1
            r -= 1