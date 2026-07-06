class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lengthOfStr = int(s[i:j]) #int at the start of each string that tells us its length
            arr.append(s[j+1:j+1+lengthOfStr])
            i = j+1+lengthOfStr

        return arr
        

