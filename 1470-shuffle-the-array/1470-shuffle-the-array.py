class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=[]
        l2=[]
        l1=nums[0:n]
        l2=nums[n:len(nums)]
        l3=[]
        for i in range(len(l1)):
    
              l3.append(l1[i])
              l3.append(l2[i])
        return(l3)