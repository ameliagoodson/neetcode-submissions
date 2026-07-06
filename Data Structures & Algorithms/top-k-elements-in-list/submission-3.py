class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # create list of empty lists 
        freq = [[] for i in range(len(nums)+1)]
        # freq = index

        # create hashmap
        for n in nums: 
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        # build up the arr: index corresponds to count of numbers
        for num, count in hashmap.items():
            freq[count].append(num)
        print(freq)

        res = []
        # iterate from the end because the last index are more
        # start at the last index, stop at 0, go backwards by -1
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



