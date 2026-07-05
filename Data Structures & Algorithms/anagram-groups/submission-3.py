class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap where the sorted str is the key and the value
        # is all of the anagram strings
        hashmap = {}
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr in hashmap:
                hashmap[sortedStr].append(string)
            else:
                hashmap[sortedStr] = [string]

        arr = []
        for key, val in hashmap.items():
            arr.append(val)
        return arr
