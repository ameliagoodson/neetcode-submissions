class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSums = [0] * (n+1) # extra index because we want to calc everything to the left of the pivot NOT INCLUDING the current index
        # we could have done i-1 but that would result in error when i = 0 so we add extra index to account for that

        # prefix i = everything summed before the number, not including it
        # build prefix sums array   
        for i in range(n):
            prefixSums[i+1] = prefixSums[i] + nums[i]

        for i in range(n):
            leftSum = prefixSums[i]
            rightSum = prefixSums[n] - leftSum - nums[i] # total - left - minus current number

            if leftSum == rightSum:
                return i
        return -1
