class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #write pointer - tracks where next valid element should go
        
        # copy every value I want to keep to the front

        for i in range(len(nums)): # read pointer
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k