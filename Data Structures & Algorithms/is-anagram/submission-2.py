class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hms={}
            hmt={}
            for i in s:
                if i not in hms:
                    hms[i]=1
                else:
                    hms[i]+=1
                
            for i in t:
                if i not in hmt:
                    hmt[i]=1
                else:
                    hmt[i]+=1
                    
            return hms==hmt
    