class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)
        print(ans)

        for num in nums:
            ans.append(num)
        
        return ans