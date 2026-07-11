class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        set1 = set(nums1)
        set2 = set(nums2)
        print(set1)
        print(set2)
        i = 0

        while i < len(nums1) and len(nums2):
            if nums1[i] in set1 and nums1[i] in set2:
                if nums1[i] not in arr:
                    arr.append(nums1[i])
            i += 1
        return arr
