class Solution:
    def wordPattern(self, a: str, s: str) -> bool:
        s=list(s.split())
        if len(s)!=len(a):
            return False
        d={}
        e={}
        for i in range(len(a)):
            if a[i] in d and d[a[i]]!=s[i]:
                return False
            if s[i] in e and e[s[i]]!=a[i]:
                return False
            e[s[i]]=a[i]
            d[a[i]]=s[i]
        return True
        