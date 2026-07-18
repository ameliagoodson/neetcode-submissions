class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        # look for unique values and write them to k

        for i in range(1, len(nums)):
            # if we find a unique value
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

