class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hm={}
           
            for i in range(len(s)):
                hm[s[i]]=hm.get(s[i],0)+1
                hm[t[i]]=hm.get(t[i],0)-1
            for value in hm.values():
                if value != 0:
                    return False
            return True