class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # something that tracks all the characters in a string 
        # hashmap of sorted chars ... iterate through str and add the sorted version to hashmap
        # hashmap contains an array of each anagram
        # compare each str (sorted) against ... is sorted(s) in hashmap. key would be sorted anagram. if yes,
        # add unsorted anagram to hashmap key

        hashmap = {}

        for word in strs:
            if "".join(sorted(word)) not in hashmap:
                hashmap["".join(sorted(word))] = [word]
            else:
                hashmap["".join(sorted(word))].append(word)

        arr = []
        
        for key, value in hashmap.items():
            arr.append(value)

        return arr
            