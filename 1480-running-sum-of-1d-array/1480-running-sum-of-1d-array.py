class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=len(nums)-1
        s=0
        l=[]
        for i in range(1,len(nums)+1):
            f=len(nums)-(len(nums)-i)
            s=0
            for j in range(f):
                s=s+nums[j]
                
            l.append(s)
        return (l)