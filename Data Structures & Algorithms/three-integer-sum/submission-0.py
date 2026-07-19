class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            # edge case if i is too high, stop
            if val > 0:
                break

            # if it's not the first value and it's not a duplicate loop again
            if i > 0 and val == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                threesum = val + nums[left] + nums[right]
                
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else: 
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # check if it's a duplicate
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            

        
        return res