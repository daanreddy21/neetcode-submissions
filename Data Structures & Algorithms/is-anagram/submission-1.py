class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for i in s:
            map[i]=map.get(i,0)+1
        for j in t:
            map[j]=map.get(j,0)-1
        for vlaue in map.values():
            if vlaue != 0:
                return False
        return True



        