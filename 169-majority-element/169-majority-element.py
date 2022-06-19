class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        for i in set(nums):
            k=nums.count(i)
            if k>c:
                c=k
                d=i
        return d
        