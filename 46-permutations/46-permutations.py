from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        l=[]
        for i in perm:
            l.append(list(i))
        return l