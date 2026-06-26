class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # store all allowed characters in hashset for O(1) lookup

        allowedChars = set(allowed)
        
        result = len(words)

        for word in words:
            for char in word:
                if char not in allowedChars:
                    result -= 1
                    break
        return result

        