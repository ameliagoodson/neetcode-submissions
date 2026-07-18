class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums2):
                hashmap[val] = i
        print(hashmap)

        arr = []

        for n in nums1:
            if n in hashmap:
                arr.append(hashmap[n])
        return arr