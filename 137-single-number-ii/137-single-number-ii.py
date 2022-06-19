class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=[]
        for i in set(nums):
             k=nums.count(i)
             if k==3:
                continue
             else:
                return i