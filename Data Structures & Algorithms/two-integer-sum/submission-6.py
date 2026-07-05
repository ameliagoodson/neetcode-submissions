class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in hash:
                return [hash[difference], i]

            if nums[i] not in hash:
                hash[nums[i]] = i
        


        # brute force O(n2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return False