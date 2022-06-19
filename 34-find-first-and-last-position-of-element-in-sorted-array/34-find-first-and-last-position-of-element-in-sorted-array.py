class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if target==nums[i]:
                l.append(i)
        if len(l)>1:
            return [l[0],l[len(l)-1]]
        elif len(l)==1:
            return [l[0],l[0]]
        else:
            return [-1,-1]