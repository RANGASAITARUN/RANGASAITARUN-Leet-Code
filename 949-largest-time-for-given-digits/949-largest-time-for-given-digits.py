from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
         perm = sorted(permutations(arr),reverse=True)
         l=[]
         for i in list(perm):
                h,i,j,k=i
                hour=(h*10+i)
                minute=(j*10+k)
                if hour<24 and minute<60:
                    return f"{h}{i}:{j}{k}"
         return ""
                
         
                