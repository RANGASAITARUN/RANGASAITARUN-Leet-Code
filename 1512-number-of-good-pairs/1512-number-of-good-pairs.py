class Solution:
    def numIdenticalPairs(self, num: List[int]) -> int:
        k=0
        for i in range(len(num)):
            for j in range(len(num)):
              if num[i]==num[j] and i<j:
                k=k+1
                
        return k