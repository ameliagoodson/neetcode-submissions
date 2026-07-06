class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        print(hashmap)
        # add each hashmap key and value as an array, to an array
        arr = []
        for key, val in hashmap.items():
            arr.append([val, key])
        arr.sort() # from smallest to highest

        print(arr)
        # remove items from the end until you have k elements
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        print(res)
        return res


