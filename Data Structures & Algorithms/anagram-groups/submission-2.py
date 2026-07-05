class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = [word]
            else:
                hashmap[sortedWord].append(word)

        arr = []
        
        for key, value in hashmap.items():
            arr.append(value)

        return arr
            