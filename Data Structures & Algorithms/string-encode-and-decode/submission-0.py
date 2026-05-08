class Solution:

    def encode(self, strs: List[str]) -> str:
        ar=[]
        for items in strs:
            strlen=len(items)
            charlen=str(strlen)
            ar.append(charlen)
            ar.append('|')
            ar.append(items)
        s ="".join(ar)
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='|':
                j+=1
            length=int(s[i:j])
            i=j+1
            word=s[i:i+length]
            res.append(word)
            i=i+length
        return res