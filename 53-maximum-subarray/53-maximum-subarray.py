class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        max=nums[0]
        for i in range(len(nums)):
           s+=nums[i]
           if s>max: 
              max=s
           if s<0:
                s=0
        return max