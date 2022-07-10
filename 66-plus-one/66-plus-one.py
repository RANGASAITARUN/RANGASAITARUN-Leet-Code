class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=[]
        for i in digits:
            k.append(str(i))
        z=int("".join(k))+1
        return ([int(x) for x in str(z)])