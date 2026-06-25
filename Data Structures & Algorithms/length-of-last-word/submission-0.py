class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # convert string to array separated by spaces
        # strip of spaces
        # get the length of the last index
        arr = s.split(" ")
        clean = []

        for word in arr:
            if word != "":
                clean.append(word)
        return len(clean[-1])
        