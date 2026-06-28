class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]": "[", "}": "{", ")": "("}

        if len(s) % 2 != 0:
            return False
        #[[[]
        
        for i, char in enumerate(s):
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    print('hi')
                    stack.pop()
                else:
                    print('hello world')
                    return False
            else:
                if i == len(s) -1:
                    return False
                else:
                    stack.append(char)
        if stack:
            return False
        else:
            return True