class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}

        # add to hashmap
        for n in nums:
            if n not in occurrences:
                occurrences[n] = 1
            else:
                occurrences[n] += 1
        
        arr = []
        for key, value in occurrences.items():
            arr.append([value, key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

