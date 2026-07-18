class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        # key is sorted str i, val is an array of anagrams

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = [word]
            else:
                hashmap[sortedWord].append(word)
        print(hashmap)
        return list(hashmap.values())

