class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in hash:
                return [hash[difference], i]
            else:
                hash[num] = i
        


        # brute force O(n2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return False