class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=[]
        l=list(s.split(" "))
        k=l[len(l)-1]
        return len(list(k))
        